import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rcParams['text.latex.preamble'] = R'\usepackage{amssymb}'
fig = plt.figure()
ax = fig.add_subplot(aspect='equal')
ax.tick_params(direction='in', color='white', labelcolor='white', grid_color='red')

fig.set_facecolor('black')
ax.set_facecolor('black')
i = np.linspace(0, 1, 100)
[_.set(color='white', linewidth=.8) for _ in fig.gca().spines.values()]
fig.tight_layout()
h = 1e-4

class Functional:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def R(self): # The radius function
        return np.sqrt(self.a**2 + self.b**2)

    def angle(self): # The angle function
        if self.a == 0 and self.b == 0:
            return None
        else:
            if self.a > 0:
                if self.b > 0:
                    return np.arctan(self.b/self.a)
                else:
                    return np.arctan(self.b/self.a)
            else:
                if self.b > 0:
                    return -np.arctan(np.abs(self.b/self.a))+np.pi
                else:
                    return np.arctan(np.abs(self.b/self.a))+np.pi

def metric_tensor(ang, raduis): # A 2x2 metric tensor to transfome from (e_x, e_y) '#636efa' basis vector to (e_r, e_theta) 'white' basis vector by given the angle and the raduis
    return np.array(
        [[np.cos(ang), -raduis*np.sin(ang)],
        [np.sin(ang), raduis*np.cos(ang)]]
    )

def simulator(a, b):
    ax.clear()
    ax.set(xlim=[-7, 7], ylim=[-7, 7])
    ax.set_xlabel('$x$ data point', color='white', size=20)
    ax.set_ylabel('$y$ data point', color='white', size=20)
    ax.set_xticks(np.arange(-7, 7, 1))
    ax.set_yticks(np.arange(-7, 7, 1))

    ax.scatter(a, b, color='#e100ff', s=15)

    ax.plot(np.cos(2*np.pi*i)*Functional(a, b).R(), # The circls radius of sqrt(a^2 + b^2)
            np.sin(2*np.pi*i)*Functional(a, b).R(),
            color='#636efa', linestyle=':', alpha=.5)
    
    ax.plot(i*a, i*b, color='#e100ff', alpha=.5, linestyle=':') # the radius of the circls in the simulation

    ax.quiver(a, b, # A vector within (e_x, e_y) '#636efa' basis vector
        1.3*(Functional(a+h, b).R()*np.cos(Functional(a+h, b).angle()) - Functional(a, b).R()*np.cos(Functional(a, b).angle()))/h,    # The first compound
        1.3*(Functional(a, b+h).R()*np.sin(Functional(a, b+h).angle()) - Functional(a, b).R()*np.sin(Functional(a, b).angle()))/h,    # The first compound
        color='yellow', scale=1, scale_units='xy', width=7**-3)
    
    c1 = 1.3*(Functional(a+h, b).R()*np.cos(Functional(a+h, b).angle()) - Functional(a, b).R()*np.cos(Functional(a, b).angle()))/h    # The first compound of yellow vector in (e_x, e_y) '#636efa' basis vector
    c2 = 1.3*(Functional(a, b+h).R()*np.sin(Functional(a, b+h).angle()) - Functional(a, b).R()*np.sin(Functional(a, b).angle()))/h    # The second compound of yellow vector in (e_x, e_y) '#636efa' basis vector
    ax.quiver(a, b, # A vector within (e_r, e_theta) 'white' basis vector
        np.array([c1, c2]) @ metric_tensor(Functional(a, b).angle(), Functional(a, b).R())[0],    # matrix multiplication # The first compound of yellow vector in (e_r, e_theta) 'white' basis vector
        np.array([c1, c2]) @ metric_tensor(Functional(a, b).angle(), Functional(a, b).R())[1],    # matrix multiplication # The second compound of yellow vector in (e_r, e_theta) 'white' basis vector
        color='yellow', scale=1, scale_units='xy', width=7**-3)    

    ax.quiver(a, b, # e_x # The derivative with respect to a
        1,    # The first compound
        0,    # The first compound
        color='white', scale=1, scale_units='xy', width=7**-3)

    ax.quiver(a, b, # e_y # The derivative with respect to b
    0,    # The first compound
    1,    # The first compound
    color='white', scale=1, scale_units='xy', width=7**-3)

    ax.quiver(a, b, # e_r # The derivative with respect to the raduis
    np.cos(Functional(a, b).angle()),    # The first compound # The metric tensor compound g_00
    np.sin(Functional(a, b).angle()),    # The first compound # The metric tensor compound g_01
    color='#636efa', scale=1, scale_units='xy', width=7**-3)

    ax.quiver(a, b, # e_theta # The derivative with respect to the angle
    -Functional(a, b).R()*np.sin(Functional(a, b).angle()),   # The first compound # The metric tensor compound g_10
    Functional(a, b).R()*np.cos(Functional(a, b).angle()),    # The first compound # The metric tensor compound g_11
    color='#636efa', scale=1, scale_units='xy', width=7**-3)

    # You cun use this part if your computer does get laggy. However, this part computes and shows the metric tensor compounds in the axes.
    '''ax.text(-13, 6.5, 'The Metric Tensor', color='white', size=16)
    ax.text(-11.5, 5.7, r'$e_r$', color='#636efa', size=15)
    ax.text(-9.8, 5.7, r'$e_{\theta}$', color='#636efa', size=15)
    ax.text(-11, 5, r'$g_{\mu\nu} = \left( \begin{array}{cc} \cos(\theta) & -r\sin(\theta) \\ \sin(\theta) & r\cos(\theta) \end{array} \right)$', 
        color='white', fontsize=14, ha='center', va='center')
    ax.text(-11, 3, fr'$g_{{\mu\nu}} = \left( \begin{{array}}{{cc}} {np.cos(Functional(a, b).angle()):.1f} & {-Functional(a, b).R()*np.sin(Functional(a, b).angle()):.1f} \\ {np.sin(Functional(a, b).angle()):.1f} & {Functional(a, b).R()*np.cos(Functional(a, b).angle()):.1f} \end{{array}} \right)$', 
        color='white', fontsize=17, ha='center', va='center')'''

    ax.grid(which='major', color='white', linewidth=.2)
    plt.draw()

def cursor(event):
    if event.inaxes is not None:
        a, b = event.xdata, event.ydata
        simulator(a, b)
    else:
        print('The cursor is in angle Interior of angle axis!')

fig.canvas.mpl_connect('motion_notify_event', cursor)
plt.show()