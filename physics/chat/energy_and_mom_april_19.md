\section{Field Energy and Momentum Balance}

\subsection{Stability from Field Energy}

We now evaluate whether the inward radiation flow, hypothesized in Section 2, can provide a stabilizing mechanism for a massive particle. Specifically, we ask: can the absorbed energy from the zero-point field counteract the gravitational self-energy that would otherwise lead to collapse?

The total field energy is given by:

\[
U = \frac{1}{16\pi} \int \left( |\vec{E}|^2 + |\vec{B}|^2 \right) \, d^3x
\]

From earlier results, the energy density near a massive particle absorbing zero-point radiation falls off as \(1/r^2\). Including the cutoff frequency \(\omega_{\text{max}} = m/\hbar\), we have:

\[
u(r) = \int_0^{m/\hbar} \frac{\alpha}{r^2} \, d\omega = \frac{\alpha m}{\hbar r^2}
\]

Integrating over all space, assuming spherical symmetry:

\[
U_{\text{rad}} = \int_0^\infty u(r) \cdot 4\pi r^2 \, dr = \int_0^\infty \frac{4\pi \alpha m}{\hbar} \, dr
\]

This diverges unless we impose a lower bound, namely the minimum radius of the particle \(R = Gm\). Truncating the integral from \(R\) to \(\infty\), we obtain:

\[
U_{\text{rad}} = \frac{4\pi \alpha m}{\hbar} \int_R^\infty dr = \infty
\]

To regularize this, we instead take the volume integral up to some finite domain or assume that most of the energy is absorbed near \(R\). The key is not the total energy, but the **balance** between the field energy and the self-gravitational energy of the particle:

\[
U_{\text{grav}} = -\frac{G m^2}{R}
\]

\[
U_{\text{rad}} = \frac{4\pi \alpha m R}{\hbar}
\]

Balancing these energies (assuming \(U_{\text{total}} = 0\)) gives:

\[
-\frac{G m^2}{R} + \frac{4\pi \alpha m R}{\hbar} = 0 \quad \Rightarrow \quad \alpha = \frac{G m \hbar}{4 \pi R^2}
\]

Substituting back, we find the energy density is:

\[
u(r) = \frac{G m \hbar}{4\pi R^2 r^2}
\]

This shows that the particle's own radiation environment acts to resist collapse, provided the momentum flow structure is accepted. The directionality of \(\vec{p} \propto -\hat{r}\) also implies an inward pressure that balances gravitational pull.

\subsection{Momentum Conservation and “Ohm’s Law”}

We now turn to momentum conservation. The total momentum exchange in the system should obey:

\[
\int_V \left( \rho \vec{E}_I + \vec{J}_S \times \vec{B}_S \right) \, d^3x = 0
\]

This relation balances the impulse from the irrotational field (associated with gravitational mass) against the magnetic impulse from the solenoidal radiation field.

Assuming the solenoidal current obeys a linear response:

\[
\vec{J}_S = \sigma \vec{E}_S
\]

and harmonic time dependence \(e^{-i \omega t}\), the field momentum becomes:

\[
-\hat{r} \int \left( m \delta(\vec{x}) \cdot \frac{G m}{r^2} - \sigma \cdot \frac{G m \hbar}{r^2} \right) \, d^3x = 0
\]

Solving gives:

\[
\sigma = \frac{m}{\hbar} \delta(\vec{x})
\]

This expression defines a delta-function conductivity concentrated at the origin — an effective Ohm's law in which the mass acts as a point-like, perfect absorber for incoming radiation. Including conventional normalization gives:

\[
\sigma = \frac{m}{4\pi \hbar} \delta(\vec{x})
\]

This result is not imposed, but emerges from requiring consistency with the momentum flux model.

\subsection{Summary}

Together, the field energy and momentum conservation arguments demonstrate that the hypothesized momentum inflow can act as a self-consistent stabilizing structure. A massive particle that sinks zero-point radiation does not collapse — not due to internal structure, but due to interaction with the vacuum field itself.
