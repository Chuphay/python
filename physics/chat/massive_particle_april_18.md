\section{Mass as a Radiation Sink: Core Hypothesis}

\subsection{Directional Momentum Flow}

We now introduce the central hypothesis of this theory: \textbf{mass acts as a sink for zero-point radiation}, producing a directional inflow of momentum from the surrounding field. This effect mimics a gravitational force and emerges naturally from the structure of the field equations.

From the previous section, we obtained the general form of the momentum in the radiation field:

\[
\vec{P}_{\text{field}} = \frac{1}{8\pi} \int_V \vec{E} \times \vec{B}^* \, d^3x = -\hat{r} \sum_{l,m} \int_V \frac{1}{4\pi} \frac{|a_E|^2 |\vec{X}_{lm}|^2}{k^2 r^2} \, d^3x
\]

Absorbing the constants, we write this compactly as:

\[
\vec{p} = -\hat{r} \frac{\alpha}{r^2}
\]

We will derive the constant \( \alpha \) in the next section. When this is done, we arrive at the key postulate of this paper:

\[
\boxed{
\vec{p} = -\hat{r} \frac{G m \hbar}{r^2}
}
\]

This expression forms the foundation of our model: \textit{mass induces a momentum flow in the surrounding zero-point field}, with a structure formally analogous to Newtonian gravity.

\subsection{Cutoff Frequency}

A further assumption is required: that this radiation sink effect only holds up to a maximum frequency. Physically, this can be interpreted as a natural limit to the energy that a given mass can absorb.

Using a simple energy balance:

\[
U = m = \hbar \omega_{\text{max}} \quad \Rightarrow \quad \omega_{\text{max}} = \frac{m}{\hbar}
\]

This cutoff ensures convergence of integrals involving radiation absorption. For ordinary matter, the corresponding frequency is many orders of magnitude above familiar scales.

\subsection{Model of a Massive Particle}

To proceed, we define what we mean by a \textit{massive particle}. The most direct classical model is a spherically symmetric mass distribution. While not a literal description of elementary particles, it provides a tractable mathematical structure.

Following Rohrlich, we consider a spherical distribution of mass density \( \rho(\vec{x}) \), with total mass:

\[
m = \int_V \rho(\vec{x}) \, d^3x
\]

In the absence of a counterbalancing force, the mass distribution would gravitationally collapse to a point. This classical result motivates the need for an external stabilizing mechanism—in our case, radiation absorption.

The gravitational self-energy of a spherically symmetric distribution is:

\[
U = -\frac{1}{2} \int \frac{G m \rho(\vec{x})}{r} \, d^3x
\]

Taking the simplest case—a thin spherical shell of radius \( R \)—yields:

\[
m = \frac{G m^2}{2 R} \quad \Rightarrow \quad R = \frac{G m}{2}
\]

Other distributions yield similar scaling. We adopt the compact form:

\[
R \sim G m
\]

This defines the minimal physical radius of a classical massive particle in this framework.

\subsubsection*{Comparison to Physical Systems}

We define the dimensionless compactness parameter:

\[
\Phi = \frac{G m}{R c^2}
\]

and compare theoretical and physical systems:

\begin{align*}
\text{Mathematical limit:} & \quad \Phi = 1 \\
\text{Black hole:} & \quad \Phi = 1 \\
\text{Sun:} & \quad \Phi \approx 2 \times 10^{-6} \\
\text{Earth:} & \quad \Phi \approx 7 \times 10^{-10} \\
\text{Proton:} & \quad \Phi \approx 1 \times 10^{-38}
\end{align*}

Real objects are far from the \( \Phi = 1 \) regime—except black holes. This scaling forms the basis for exploring high-density limits in our theory.

\subsection{Energy Conservation and Stability}

We now demonstrate that a massive particle can remain stable, due to energy exchange with the radiation field.

\subsubsection*{Field Energy}

The total energy stored in the surrounding radiation field is:

\[
U = \frac{1}{16\pi} \int \left( |\vec{E}|^2 + |\vec{B}|^2 \right) \, d^3x
\]

From our earlier solutions, this becomes:

\[
U = \sum_{l,m} \int_V \frac{1}{4\pi} \frac{|a_E|^2 |\vec{X}_{lm}|^2}{k^2 r^2} \, d^3x
\]

Defining the energy density:

\[
u(r) = \sum_{l,m} \frac{1}{4\pi} \frac{|a_E|^2 |\vec{X}_{lm}|^2}{k^2 r^2} = \frac{\alpha}{r^2}
\]

and applying the frequency cutoff:

\[
u(r) = \int_0^{m/\hbar} \frac{\alpha}{r^2} \, d\omega = \frac{\alpha m}{\hbar r^2}
\]

\subsubsection*{Total Energy and Balance}

The total energy is then:

\[
U = \int_V u(r) \, d^3x = -\frac{G m^2}{R} + \frac{4 \pi \alpha m R}{\hbar}
\]

Enforcing energy conservation:

\[
U_{\text{total}} = 0 \quad \Rightarrow \quad \alpha = \frac{1}{4 \pi R^2} G m \hbar
\]

Substitute into \( u(r) \):

\[
u(r) = \frac{G m \hbar}{4 \pi R^2 r^2}
\]

This supports the view that the field dynamically stabilizes the mass by opposing gravitational collapse.

\subsection{Momentum Conservation and Effective Conductivity}

To complete the consistency check, we examine momentum conservation and derive an effective Ohm’s law.

\subsubsection*{Momentum Balance}

From Jackson Eq. 6.114:

\[
\int_V \left( \rho \vec{E}_I + \vec{J}_S \times \vec{B}_S \right) \, d^3x = 0
\]

\subsubsection*{Ohm’s Law}

Assume:

\[
\vec{J}_S = \sigma \vec{E}_S
\]

and harmonic time dependence. Evaluate:

\[
-\hat{r} \int_V \left( m \delta(\vec{x}) \cdot \frac{G m}{r^2} - \sigma \cdot \frac{G m \hbar}{r^2} \right) \, d^3x = 0
\]

Solving:

\[
\sigma = \frac{m}{\hbar} \delta(\vec{x}) \quad \text{or} \quad \sigma = \frac{m}{4 \pi \hbar} \delta(\vec{x})
\]

\subsubsection*{Interpretation}

This implies the massive particle has a localized delta-function conductivity at the origin. This emerges naturally from conservation laws and further supports the central hypothesis: \textit{mass interacts with the radiation field as a sink, leading to a self-consistent stabilization of the particle.}

