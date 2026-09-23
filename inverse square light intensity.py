"""
Modelling the inverse square law for a finite-size Lambertian light source
----------------------------------------------------------------------------
Compares three things against real lux meter data taken at 10 distances
from a small LED torch:

  1. The simple point-source inverse square law:   E(r) = k / r**2
  2. A closed-form finite-disc-source model:        E(r) = pi*L*a**2 / (a**2 + r**2)
  3. A direct numerical double integral over the disc, as a check on (2).

Run with: python inverse_square_simulation.py
Requires: numpy, scipy, matplotlib
"""

import numpy as np
from scipy import integrate, optimize
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Experimental data (lux meter readings vs. distance)
# ---------------------------------------------------------------
distances_m = np.array([0.30, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.50, 3.00])
lux_readings = np.array([585, 214, 95, 54, 35, 24, 18, 14, 9, 7])

# ---------------------------------------------------------------
# 2. Fit the simple point-source model  E = k / r^2  to the data
# ---------------------------------------------------------------
def point_source_model(r, k):
    return k / r**2

k_fit, _ = optimize.curve_fit(point_source_model, distances_m, lux_readings)
k_fit = k_fit[0]
print(f"Best-fit k for point-source model: {k_fit:.2f} lux*m^2")

ss_res = np.sum((lux_readings - point_source_model(distances_m, k_fit)) ** 2)
ss_tot = np.sum((lux_readings - lux_readings.mean()) ** 2)
r_squared = 1 - ss_res / ss_tot
print(f"R^2 of the point-source fit: {r_squared:.4f}")

# ---------------------------------------------------------------
# 3. Finite Lambertian disc source: closed-form and numerical integral
# ---------------------------------------------------------------
a = 0.004  # assumed source radius in metres (a few mm, roughly an LED die)
L = k_fit / (np.pi * a ** 2)  # radiance chosen so the far-field k matches the fit


def closed_form_disc(r, a, L):
    """Analytic on-axis illuminance from a uniform Lambertian disc of radius a."""
    return np.pi * L * a ** 2 / (a ** 2 + r ** 2)


def integrand(rho, r, L):
    """Contribution of an annulus at radius rho (already integrated over phi)."""
    return 2 * np.pi * L * r ** 2 * rho / (rho ** 2 + r ** 2) ** 2


def numerical_disc(r, a, L):
    """Numerically integrate the same double integral using scipy.quad."""
    value, _ = integrate.quad(integrand, 0, a, args=(r, L))
    return value


print("\n r (m)   point-source   closed-form disc   numerical integral")
for r in distances_m:
    ps = point_source_model(r, k_fit)
    cf = closed_form_disc(r, a, L)
    num = numerical_disc(r, a, L)
    print(f" {r:5.2f}   {ps:10.3f}     {cf:10.3f}          {num:10.3f}")

# ---------------------------------------------------------------
# 4. Plot everything together
# ---------------------------------------------------------------
r_fine = np.linspace(0.2, 3.2, 300)

plt.figure(figsize=(7, 5))
plt.plot(r_fine, point_source_model(r_fine, k_fit), "--",
         label="Point-source model (E = k/r²)")
plt.plot(r_fine, closed_form_disc(r_fine, a, L), "-",
         label="Finite disc source (closed form)")
plt.scatter(distances_m, lux_readings, color="black", zorder=5,
            label="Measured (lux meter)")
plt.xlabel("Distance from source, r (m)")
plt.ylabel("Illuminance (lux)")
plt.title("Illuminance vs distance: measured data vs. modelled curves")
plt.legend()
plt.tight_layout()
plt.savefig("inverse_square_comparison.png", dpi=150)
print("\nPlot saved to inverse_square_comparison.png")
