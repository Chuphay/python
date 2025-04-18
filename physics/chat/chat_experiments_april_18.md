\section{Classical Experimental Tests}

This section demonstrates that the present theory reproduces three key experimental predictions of general relativity: the precession of Mercury's perihelion, the deflection of light near a massive object, and gravitational redshift. Each is derived from the momentum-transfer hypothesis introduced earlier.

\subsection{Precession of the Perihelion of Mercury}

In electrodynamics, a static Coulomb field transforms under Lorentz boosts into a configuration with both electric and magnetic components. Specifically, the fields of a charge moving at velocity \( \vec{v} \) are:

\[
\vec{E}' = \gamma \vec{E} - \frac{\gamma^2}{\gamma + 1} \vec{v} (\vec{v} \cdot \vec{E}), \quad
\vec{B}' = - \gamma \vec{v} \times \vec{E}
\]

where \( \gamma = 1 / \sqrt{1 - v^2} \).

By analogy, we assume the same Lorentz transformation laws apply to gravity. We define the gravitational field:

\[
\vec{E}_g = \vec{F} / m = - \frac{G M}{r^3} \vec{r}
\]

Then, under a Lorentz boost:

\[
\vec{E}_g' = \gamma \vec{E}_g - \frac{\gamma^2}{\gamma + 1} \vec{v} (\vec{v} \cdot \vec{E}_g), \quad
\vec{B}_g' = -\gamma \vec{v} \times \vec{E}_g
\]

In the low-velocity limit \( v \ll 1 \), we find:

\[
\vec{B}_g = - \vec{v} \times \vec{r} \cdot \frac{GM}{r^3}
\]

This introduces a "gravitomagnetic" interaction analogous to magnetism in electrodynamics.

We now consider Kepler’s problem. The Newtonian effective potential is:

\[
U_{\text{Newt}} = \frac{1}{2} m \left( \frac{dr}{dt} \right)^2 - \frac{GMm}{r} + \frac{l^2}{2 m r^2}
\]

where \( l = m |\vec{r} \times \vec{v}| \) is the orbital angular momentum.

A moving charge induces a magnetic moment \( \vec{m} = \frac{1}{2} e (\vec{r} \times \vec{v}) \). Replacing \( e \rightarrow m \), we define a gravitational magnetic moment:

\[
\vec{m}_g = \frac{1}{2} m (\vec{r} \times \vec{v})
\]

The potential energy of this moment in a magnetic field is:

\[
U = -\vec{m}_g \cdot \vec{B}_g = -\frac{GM m}{2} |\vec{r} \times \vec{v}|^2 / r^3
\]

This adds a correction to the potential energy. Including the reciprocal effect (from the motion of the central mass), we double this term and find the corrected potential:

\[
U_{\text{Einstein}} = \frac{1}{2} m \left( \frac{dr}{dt} \right)^2 - \frac{GMm}{r}
+ \frac{l^2}{2 m r^2} - \frac{GM l^2}{m r^3}
\]

This is the same correction obtained in general relativity to first order. As Carroll notes, general relativity produces this result exactly; in our theory, it emerges as a first-order approximation. Higher-order terms may offer a route to testing deviations.

\subsection{Deflection of Light}

We now consider the bending of light near a massive object. Our central hypothesis is that mass creates a momentum-transfer field:

\[
\vec{P}(r) = - \hat{r} \frac{G m \hbar}{r^2}
\]

A photon traveling through this field receives a cumulative momentum shift:

\[
\Delta \vec{p} = \int_{\text{path}} \vec{P}(r) \, dl
\]

Assuming a straight-line path passing at minimum distance \( b \), we integrate:

\[
\Delta \vec{p} = \int_{-\infty}^{\infty} - \frac{G m \hbar}{r^3} \vec{r} \, w \, dz
\]

The parallel momentum shifts cancel symmetrically. The transverse component yields:

\[
\Delta p_y = \hbar w \cdot \frac{2 G m}{b}
\]

The angle of deflection is then:

\[
\theta \approx \frac{\Delta p_y}{p_z} = \frac{2 G m}{b} \quad \Rightarrow \quad \alpha = \frac{4 G m}{b}
\]

This matches the deflection angle predicted by general relativity.

\subsection{Gravitational Redshift}

Finally, we consider the redshift of light climbing out of a gravitational well. As before, a photon gains or loses momentum depending on its path through the momentum field.

Using:

\[
\Delta p = \int_{\infty}^{R} \vec{P} \cdot \hat{r} \cdot w \, dr = \int_{\infty}^{R} - \frac{G m \hbar}{r^2} w \, dr = \hbar w \cdot \frac{G m}{R}
\]

The resulting frequency shift is:

\[
\hbar w' = \hbar w + \Delta p = \hbar w \left( 1 + \frac{G m}{R} \right)
\]

which, to first order, matches the prediction of general relativity for gravitational redshift.
