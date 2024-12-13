#import math

import matplotlib.pyplot as plt
import numpy as np

# Define the matrix (2x2 for simplicity)
translation_matrix = np.array([[1, 0, 0],
                               [0, 1, 0],
                               [4, 5, 1]])  # shift origin to 4, 5
# Define the vector
base_vector = np.array([1, 1, 0])  # goes to (1, 1)

# Perform the matrix-vector multiplication
result_vector = np.dot(base_vector, translation_matrix)


# # Function to plot vectors in 3D
# def plot_vector_3d(ax, vec, color, label):
#     ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label)
#


# Function to plot vectors in 2D
def plot_vector_2d(ax, vec, color, label):
    ax.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

# Plot the original and transformed vectors
plot_vector_2d(ax, base_vector, 'blue', 'Original Vector')
#plot_vector_3d(ax, result_vector, 'red', 'Transformed Vector')

# Add legend
plt.legend()
plt.title("Vector Transformations - Computer Graphics")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
