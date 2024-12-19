# Polar Coordinates Transformation and Metric Tensor Simulation

This project visualizes the transformation of vectors in polar coordinates, utilizing a metric tensor to transform vectors from the Cartesian basis $(e_x, e_y)$ to the polar basis $(e_r, e_\theta)$. The simulation computes the radius and angle of a point in the 2D plane and transforms vector components between these coordinate systems.

## Mathematical Framework

### 1. **Polar Coordinates Transformation**
Given a point in Cartesian coordinates $(a, b)$, its **radius** $r$ and **angle** $\theta$ in polar coordinates are defined as:

$$
r = \sqrt{a^2 + b^2}
$$

$$
\theta = \arctan(\frac{b}{a})
$$

where $\text{atan2}(b, a)$ is the 2-argument arctangent function that gives the angle $\theta$ of the point $(a, b)$ relative to the positive x-axis.

### 2. **Metric Tensor**
The **metric tensor** $g_{\mu\nu}$ is used to transform vectors from the Cartesian basis $(e_x, e_y)$ to the polar basis $(e_r, e_\theta)$. The general form of the metric tensor for polar coordinates is:

$$
g_{\mu\nu} = \begin{pmatrix} 
\cos(\theta) & -r\sin(\theta) \\
\sin(\theta) & r\cos(\theta)
\end{pmatrix}
$$

This tensor maps derivatives in the Cartesian basis to derivatives in the polar basis. The individual components of the tensor are:

- $g_{00} = \cos(\theta)$
- $g_{01} = -r\sin(\theta)$
- $g_{10} = \sin(\theta)$
- $g_{11} = r\cos(\theta)$

### 3. **Vector Derivatives**
The code computes finite difference approximations of the derivatives of the radius and angle with respect to the Cartesian coordinates $a$ and $b$. These are used to visualize vector fields and their components in both the Cartesian and polar basis:

$$
\frac{\partial r}{\partial a} \approx \frac{r(a+h, b) - r(a, b)}{h}
$$

where $h$ is a small perturbation. The same concept applies for other derivatives, such as $\frac{\partial r}{\partial b}$.

### 4. **Transformation of Vectors**
The yellow vectors in the plot represent transformed derivatives and are calculated using the metric tensor:

$$
\mathbf{V} = \begin{pmatrix} c_0 \\\ c_1 \end{pmatrix} \cdot \begin{pmatrix} g_{00} & g_{01} \\\ g_{10} & g_{11} \end{pmatrix} = \begin{pmatrix} c_0g_{00} + c_1g_{10} \\\ c_0g_{01} + c_1g_{11} \end{pmatrix}
$$

where $c_1$ and $c_2$ are the components of the vector in Cartesian coordinates, and the matrix multiplication transforms it to polar coordinates.

### 5. **Simulating and Plotting**
- **Circles** are plotted using parametric equations in polar coordinates:

$$
x = r \cos(2\pi t), \quad y = r \sin(2\pi t)
$$

- **Vector Field**: The simulation visualizes the vectors that represent derivatives with respect to $a$, $b$, $r$, and $\theta$ in both Cartesian and polar coordinate systems.

## Code Overview

The simulation is implemented using Python with the `matplotlib` library for plotting and `numpy` for numerical computations. The simulation updates dynamically based on the cursor position in the plot, computing and displaying vectors, circles, and metric tensor components.

## Setup and Requirements

- Python 3.x
- `matplotlib`
- `numpy`
- LaTeX environment for rendering mathematical formulas in plots

## Running the Code

1. Install the required dependencies:

```bash
pip install matplotlib numpy
