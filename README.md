# Linear Transformation and Metric Tensor Simulation

This document describes the simulation of a linear transformation and its corresponding metric tensor in polar coordinates using a Python script.

## Overview

The program simulates the transformation of vectors in a 2D Cartesian coordinate system to polar coordinates. It computes the metric tensor for the transformation and visualizes it. The transformation is represented using a linear combination of the radial and angular components in polar coordinates. The following aspects are discussed:

1. **Radius Function**: The function $R(a, b) = \sqrt{a^2 + b^2}$ represents the radius in polar coordinates.
2. **Angle Function**: The angle function $\theta$ is computed using the arctangent function.

### Metric Tensor

The metric tensor is a mathematical object that defines how distances are measured in a curved space. For the transformation from Cartesian to polar coordinates, the metric tensor is given by the following matrix:

$$
M = \begin{pmatrix}
\cos(\theta) & -r\sin(\theta) \\
\sin(\theta) & r\cos(\theta)
\end{pmatrix}
$$

The inverse of the metric tensor is:

$$
M^{-1} = \begin{pmatrix}
\cos(\theta) & \sin(\theta) \\
-\frac{1}{r}\sin(\theta) & \frac{1}{r}\cos(\theta)
\end{pmatrix}
$$

Where:
- $r = \sqrt{a^2 + b^2}$ is the radial distance.
- $\theta$ is the angle calculated as $\theta = \arctan(\frac{b}{a})$.

### Components of the Metric Tensor

The metric tensor components are crucial for transforming vectors between Cartesian and polar coordinates. The components are calculated as:

$$
g_{\mu\nu} = \begin{pmatrix}
1 & 0 \\
0 & r^2
\end{pmatrix}
$$

The inverse metric tensor components are:

$$
g^{\mu\nu} = \begin{pmatrix}
1 & 0 \\
0 & \frac{1}{r^2}
\end{pmatrix}
$$

### Visualizing the Transformation

The Python script visualizes the transformation by displaying:
- A scatter plot of points $(a, b)$.
- The radial and angular components of the transformation.
- The metric tensor components in both Cartesian and polar coordinate systems.
- The vectors in both the Cartesian basis $(e_x, e_y)$ and polar basis $(e_r, e_\theta)$.

## Conclusion

This simulation helps to understand the transformation of vectors between different coordinate systems, particularly from Cartesian to polar coordinates, and how the metric tensor is involved in this transformation.
