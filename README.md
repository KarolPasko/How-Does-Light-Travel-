#  How Light Travels

> **An exploration of the physics and mathematics behind light, written from a theatrical lighting designer's perspective.**

This repository bridges the gap between abstract electromagnetic theory and the physical equipment found on a stage rig. It breaks down the math governing how light waves propagate, bend, and focus, laying the groundwork for interactive Python simulation models.

---

##  Creative Context vs. Technical Reality

| What We See Behind the Desk | What is Actually Happening |
| :--- | :--- |
| **Instant beams** cutting through haze. | Self-sustaining fields traveling at c ≈ 3 × 10⁸ m/s. |
| **Warm amber vs. deep blue** gels. | Identical physical phenomena oscillating at different frequencies (c = fλ). |
| **Sharp profile cuts vs. soft Fresnel washes.** | Piecewise applications of Snell's Law across curved or stepped glass. |

---

## The Mathematical Framework

<details>
<summary><b> Click to expand the physics equations running under the hood</b></summary>

### 1. Maxwell's Wave Equation
Proves light is an electromagnetic wave that requires no medium to travel through space:
```math
c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.998 \times 10^8 \text{ m/s}
```

### 2. Wave Mechanics & Colour
Expresses light as an oscillating sine function where variations in wavelength (λ) dictate visible colour (400nm to 700nm):
```math
E(x,t) = E_0 \sin(kx - \omega t)
```

### 3. Reflection & Snell's Law
The geometric foundation of beam targeting and lens refraction, tracking how light changes direction based on the refractive index (n = c/v):
```math
\theta_i = \theta_r \quad \text{and} \quad n_1 \sin \theta_1 = n_2 \sin \theta_2
```

### 4. The Lensmaker's Equation
The exact rule utilized by Augustin-Jean Fresnel to collapse heavy plano-convex lenses into lightweight, concentric stepped rings:
```math
\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)
```
</details>

---

## Upcoming Python Modeling Intentions
The core goal of the accompanying code inside this repository is to turn these equations into interactive tools:
* **Ray Tracing Simulator:** Visualise vector trajectories as they hit mirrors and lenses using `NumPy`.
* **Fresnel Lens Model:** Step-by-step geometric calculation of how concentric glass rings redirect rays to a single focal point.
* **Wave Interference Engine:** Plot shifting wave amplitudes over discrete time steps (t) using `Matplotlib`.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
