import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# inital value condition
y0 = [10, 1]

# tRange
t = np.linspace(0, 50, num=1000)

# Our different parameters that vary
alpha = 1.1
beta = .4
delta = .1
gamma = .4

params = [alpha, beta, delta, gamma]

# defining the ODE of the predator prey model


def sim(variables, t, params):
    x = variables[0]

    y = variables[1]

    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y

    return ([dxdt, dydt])


# Changing alpha to create different lines on the graph
y = odeint(sim, y0, t, args=(params,))


params = [.9, beta, delta, 1]
y2 = odeint(sim, y0, t, args=(params,))


params = [1.3, .5, delta, gamma]
y3 = odeint(sim, y0, t, args=(params,))


f, (ax1) = plt.subplots(1)

line1, = ax1.plot(y[:, 0], y[:, 1], color="b", label="alpha = 1.1")
line2, = ax1.plot(y2[:, 0], y2[:, 1], color="r", label="alpha = .9")
line3, = ax1.plot(y3[:, 0], y3[:, 1], color="g", label="alpha = 1.3")

legend = plt.legend()

ax1.set_xlabel("Prey")
ax1.set_ylabel("Predator")


plt.show()
