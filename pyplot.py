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

plt.figure()  # creates a new figure
plt.plot(x, y)
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()

plt.figure()  # creates a new figure
plt.plot(x, y)  # by default, the third argument is 'b-' (blue line)
plt.plot(x, y, 'ro')  # red dots
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()


# We can be more explicit with the arguments:
plt.figure()  # creates a new figure
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
plt.figure()  # creates a new figure
plt.plot(a1)
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()

# Plotting a two-dimensional array:
a2 = np.random.randint(0, 100, 10).reshape(2, 5)
plt.figure()  # creates a new figure
plt.plot(a2[0], a2[1])
plt.xlabel("x-axis personalized label")
plt.ylabel("y-axis personalized label")
plt.show()

# Histogram of a one-dimensional numpy array:
a3 = np.random.randint(0, 100, 50)
plt.figure()  # creates a new figure
plt.hist(a3)
plt.show()

plt.figure()  # creates a new figure
plt.hist(a3, cumulative=True)
plt.show()


# ========================================== #
# Plotting various subplots in a single plot #
# ========================================== #

x = np.random.randint(0, 100, 10)

plt.figure()  # creates a new figure

plt.subplot(2, 2, 1)  # nrows, ncols, index
plt.plot(x, x)
plt.title("Linear")

plt.subplot(2, 2, 2)  # nrows, ncols, index
plt.plot(x, x * x)
plt.title("Squared")

plt.subplot(2, 2, 3)  # nrows, ncols, index
plt.plot(x, x ** 3)
plt.title("Cubic")

plt.subplot(2, 2, 4)  # nrows, ncols, index
plt.plot(x, x ** 4)
plt.title("Quartic")

plt.show()
