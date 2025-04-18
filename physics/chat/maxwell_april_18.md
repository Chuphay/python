\section{Maxwell Equations}

\subsection{From Electromagnetism to Gravitoelectromagnetism}

We assume that gravity is governed by Maxwell-like field equations:

\[
\nabla \times \vec{B} - \partial_t \vec{E} = -4 \pi G \vec{J}, \quad \nabla \times \vec{E} + \partial_t \vec{B} = 0
\]

\[
\nabla \cdot \vec{E} = -4 \pi G \rho, \quad \nabla \cdot \vec{B} = 0
\]

and, for completeness, the continuity equation for mass-current:

\[
\nabla \cdot \vec{J} + \partial_t \rho = 0
\]

We are using units where \( c = 1 \). In SI units, the gravitational constant is:

\[
G = 6.674 \times 10^{-11} \, \mathrm{N \cdot m^2 / kg^2}
\]

\subsection{Solenoidal and Irrotational Components}

Any vector field \( \vec{V} \) can be decomposed into solenoidal and irrotational parts:

\[
\vec{V} = \vec{V}_I + \vec{V}_S
\]

with

\[
\nabla \cdot \vec{V}_S = 0, \quad \nabla \times \vec{V}_I = 0
\]

This allows us to split the field equations into two decoupled systems:

\textbf{Irrotational (Static fields):}

\[
\nabla \cdot \vec{E}_I = -4 \pi G \rho
\]

\[
\partial_t \vec{E}_I = 4 \pi G \vec{J}_I
\]

\[
\nabla \cdot \vec{J}_I + \partial_t \rho = 0
\]

\textbf{Solenoidal (Radiation fields):}

\[
\nabla \times \vec{E}_S + \partial_t \vec{B}_S = 0
\]

\[
\nabla \times \vec{B}_S - \partial_t \vec{E}_S = -4 \pi G \vec{J}_S
\]

In the rest frame of the massive object (the frame used throughout this paper), these equations decouple neatly. We can define a rescaled solenoidal current:

\[
\vec{J}_S' = -G \vec{J}_S
\]

This simplifies the radiation equations to a more standard form:

\[
\nabla \times \vec{B}_S - \partial_t \vec{E}_S = 4 \pi \vec{J}_S'
\]

Since this affects no other equations, and matches familiar radiation formulations, we drop the prime and use:

\[
\nabla \times \vec{B}_S - \partial_t \vec{E}_S = 4 \pi \vec{J}_S
\]

\[
\nabla \times \vec{E}_S + \partial_t \vec{B}_S = 0
\]


\section{Solutions to the Maxwell Equations}

\subsection{Vector Spherical Harmonics}

Following Berrara~\cite{berrara1985}, any vector field \( \vec{V}(\vec{x}) \) and scalar field \( g(\vec{x}) \) can be expanded in terms of vector spherical harmonics:

\[
\vec{V}(\vec{x}) = \sum_{l=0}^\infty \sum_{m=-l}^{l} \left[
a_{lm}(r) \vec{Y}_{lm}(\theta, \phi)
+ b_{lm}(r) \left( \hat{r} \times \vec{X}_{lm}(\theta, \phi) \right)
+ c_{lm}(r) \vec{X}_{lm}(\theta, \phi)
\right]
\]

\[
g(\vec{x}) = \sum_{l=0}^\infty \sum_{m=-l}^{l} g_{lm}(r) Y_{lm}(\theta, \phi)
\]

where \( \vec{Y}_{lm} = \hat{r} Y_{lm} \), and

\[
\vec{X}_{lm}(\theta, \phi) = \frac{-i}{\sqrt{l(l+1)}} \vec{r} \times \nabla Y_{lm}(\theta, \phi)
\]

A collection of useful identities involving these harmonics is provided in the Appendix.

\subsection{Newtonian Gravity from the Irrotational Field}

To recover Newton's law, we assume a static point source:

\[
\rho(\vec{x}) = m \delta^3(\vec{x})
\]

From the irrotational field equations:

\[
\nabla \cdot \vec{E}_I = -4 \pi G \rho, \quad \nabla \times \vec{E}_I = 0
\]

we expand \( \vec{E}_I \) as:

\[
\vec{E}_I = \sum_{l,m} \left[
a_{lm}(r) \vec{Y}_{lm}
+ b_{lm}(r) (\hat{r} \times \vec{X}_{lm})
+ c_{lm}(r) \vec{X}_{lm}
\right]
\]

The curl-free condition implies:

\[
c_{lm} = 0
\]

\[
a_{lm} = - \frac{i}{\sqrt{l(l+1)}} \frac{d}{dr}(r b_{lm})
\]

The divergence equation becomes:

\[
4 \pi G \sum_{l,m} \rho_{lm} Y_{lm}
= \sum_{l,m} \left[
\frac{1}{r^2} \frac{d}{dr}(r^2 a_{lm}) - i \sqrt{l(l+1)} \frac{b_{lm}}{r}
\right] Y_{lm}
\]

Define:

\[
B_{lm}(r) = \frac{i r b_{lm}}{\sqrt{l(l+1)}}
\]

Then we obtain the standard differential equation:

\[
\frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{d B_{lm}}{dr} \right) - \frac{l(l+1)}{r^2} B_{lm} = 4 \pi G \rho_{lm}
\]

whose solution is:

\[
B_{lm}(r) = - \frac{4 \pi G q_{lm}}{(2l + 1) r^{l+1}}, \quad \text{where} \quad q_{lm} = \int Y_{lm}^*(\theta, \phi) r^l \rho(\vec{x}) \, d^3x
\]

The resulting field is:

\[
\vec{E}_I(\vec{x}) = \sum_{l,m} \left[
- \frac{4\pi i G}{2l+1} \frac{q_{lm}}{r^{l+2}} \sqrt{l(l+1)} (\hat{r} \times \vec{X}_{lm})
- \frac{4\pi G (l+1)}{2l+1} \frac{q_{lm}}{r^{l+2}} \vec{Y}_{lm}
\right]
\]

In the monopole case:

\[
\rho(\vec{x}) = m \delta^3(\vec{x}) \quad \Rightarrow \quad \vec{E}_I(\vec{x}) = - \frac{G m}{r^2} \hat{r}
\]

as expected from Newtonian gravity.

\subsection{Radiation from the Solenoidal Field}

In vacuum (i.e., outside a massive particle), the solenoidal field equations become:

\[
\nabla \times \vec{E}_S + \partial_t \vec{B}_S = 0, \quad
\nabla \times \vec{B}_S - \partial_t \vec{E}_S = 0
\]

Assuming a time dependence \( e^{-i \omega t} \), the general solution is:

\[
\vec{B}_S = \sum_{l,m} \left[
a_E(l,m) f_l(kr) \vec{X}_{lm}
- \frac{i}{k} a_M(l,m) \nabla \times \left( g_l(kr) \vec{X}_{lm} \right)
\right]
\]

\[
\vec{E}_S = \sum_{l,m} \left[
\frac{i}{k} a_E(l,m) \nabla \times \left( f_l(kr) \vec{X}_{lm} \right)
+ a_M(l,m) g_l(kr) \vec{X}_{lm}
\right]
\]

The functions \( f_l \) and \( g_l \) are linear combinations of spherical Hankel functions:

\[
h_l^{(1)}(x) = -i (-x)^l \left( \frac{1}{x} \frac{d}{dx} \right)^l \left( \frac{e^{ix}}{x} \right), \quad h_l^{(2)}(x) = \left( h_l^{(1)}(x) \right)^*
\]

Since the particle is assumed to be a radiation sink, only **incoming waves** are used.

The instantaneous power absorbed is:

\[
P = \int_V \nabla \cdot \left( \frac{1}{8\pi} \vec{E} \times \vec{B}^* \right) d^3x
= R^2 \int \hat{r} \cdot \vec{S} \, d\Omega \Big|_{r=R}
\]

Using the orthogonality of the harmonics:

\[
P = \frac{R^2}{8 \pi} \sum_{l,m} \left[
\frac{-i}{k} |a_E|^2 h_l^{(2)} \frac{1}{r} \frac{d}{dr}(r h_l^{(1)})
+ \frac{i}{k} |a_M|^2 h_l^{(1)} \frac{1}{r} \frac{d}{dr}(r h_l^{(2)})
\right]_{r=R}
\]

Assuming the particle is electromagnetically neutral on average, we set \( |a_E|^2 = |a_M|^2 \). Using the Wronskian simplifies the result to:

\[
P = \sum_{l,m} \frac{|a_E|^2}{4 \pi k^2}
\]

To compute the energy in the field (using the \( 1/r \) radiation zone approximation):

\[
\vec{B} \approx \sum_{l,m} \left[
a_E f_l(kr) \vec{X}_{lm}
+ a_M g_l(kr) (\hat{r} \times \vec{X}_{lm})
\right], \quad
\vec{E} \approx - \hat{r} \times \vec{B}
\]

Assuming:

\[
|f_l|^2 = |g_l|^2 = \frac{1}{k^2 r^2}
\]

The energy density in a spherical shell at \( r = R \) is:

\[
\frac{dU}{dr} \Big|_{r=R} = \frac{1}{16\pi} \int \left( |\vec{E}|^2 + |\vec{B}|^2 \right) r^2 d\Omega = \sum_{l,m} \frac{1}{8\pi} \frac{|a_E|^2}{k^2}
\]

The total field momentum:

\[
\vec{P}_{\text{field}} = \frac{1}{8\pi} \int_V \vec{E} \times \vec{B}^* \, d^3x
= -\hat{r} \sum_{l,m} \int_V \frac{|a_E|^2 |\vec{X}_{lm}|^2}{4\pi k^2 r^2} \, d^3x
\]

The specific coefficients \( |a_E|^2 \) will be fixed by boundary conditions in the section on collapse and stability.
