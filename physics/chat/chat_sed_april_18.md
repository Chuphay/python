\section{Stochastic Electrodynamics (SED)}

We assume that the vacuum is not empty, but filled with a Lorentz-invariant zero-point electromagnetic field, even at absolute zero. This is the core hypothesis of Stochastic Electrodynamics (SED), a classical theory that adds a stochastic background field to Maxwell's equations.

The spectral energy density of the vacuum field is:

$$\rho(\omega) = \frac{1}{2} \hbar \omega$$

This field is modeled as a classical stochastic process with Gaussian statistics. In Cartesian coordinates, the electric and magnetic fields take the form:

$$
\vec E (\vec x ,  t) = \text{Re} \sum_{\lambda = 1}^2  \int d^3k ~ \hat \epsilon(\vec k, \lambda) \sqrt {\frac {\hbar \omega} {2 \pi^2}} W_{\lambda}(\vec k) e^{i(\omega t - \vec k \cdot \vec x)}
$$

$$
\vec B (\vec x ,  t) = \text{Re} \sum_{\lambda = 1}^2  \int d^3k ~ \frac {\vec k \times \hat \epsilon(\vec k, \lambda)}{k} \sqrt {\frac {\hbar \omega} {2 \pi^2}} W_{\lambda}(\vec k) e^{i(\omega t - \vec k \cdot \vec x)}
$$

The random variables \( W_\lambda(\vec k) \) satisfy:

$$\langle W \rangle = 0, \qquad \langle W_i(\vec k) W_j^*(\vec k') \rangle = \delta_{ij} \delta^3(\vec k - \vec k')$$

This stochastic field gives rise to forces that can stabilize classical systems, and we will assume throughout the rest of the paper that mass interacts with this field by sinking a portion of its energy.
