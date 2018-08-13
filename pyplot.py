#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Introduction to the pyplot interface """

import numpy as np
import matplotlib.pyplot as plt


# =============== #
# Plotting points #
# =============== #

# We can use tuples or lists
x = (1, 2, 3, 4)  # x values as a tuple
y = [1, 4, 9, 16]  # y values as a list

plt.plot(x, y)
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()


plt.plot(x, y)  # by default, the third argument is 'b-' (blue line)
plt.plot(x, y, 'ro')  # red dots
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()


# We can be more explicit with the arguments:
plt.plot(x, y, color='green', marker='o',
         linestyle='dashed', linewidth=2, markersize=12)
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()


# ===================== #
# Plotting numpy arrays #
# ===================== #

# Plotting a one-dimensional array:
a1 = np.random.randint(0, 100, 10)
plt.plot(a1)
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()

# Plotting a two-dimensional array:
a2 = np.random.randint(0, 100, 10).reshape(2, 5)
plt.plot(a2[0], a2[1])
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()

# Histogram of a one-dimensional numpy array:
a3 = np.random.randint(0, 100, 50)
plt.hist(a3)
plt.show()

plt.hist(a3, cumulative=True)
plt.show()


# ========================================== #
# Plotting various subplots in a single plot #
# ========================================== #

# Plotting various plots in the same figure:
x = np.random.randint(0, 100, 10)

fig, axes = plt.subplots(ncols=2, nrows=2)
ax0, ax1, ax2, ax3 = axes.flatten()

ax0.plot(x, x)
ax0.set_title('Linear')

ax1.plot(x, x * x)
ax1.set_title('Squared')

ax2.plot(x, x ** 3)
ax2.set_title('Cubic')

ax3.plot(x, x ** 4)
ax3.set_title('Quartic')

fig.tight_layout()
plt.show()
