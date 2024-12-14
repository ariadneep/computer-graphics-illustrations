import matplotlib.pyplot as plt
import numpy as np

# Define the matrix (2x2 for simplicity)
translation_matrix = np.array([[1, 0, 0],
                               [0, 1, 0],
                               [4, 5, 1]])  # shift origin to 4, 5
# Define the vector
base_vector = np.array([1, 1, 1])  # goes to (1, 1)

# Perform the matrix-vector multiplication
result_vector = np.dot(base_vector, translation_matrix)
print(result_vector)


def plot_vector_2d(ax, origin, end, color, label):
    ax.quiver(origin[0], origin[1], end[0], end[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)


# Set up the 2D plot
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_aspect('equal')

# Plot the original vector and the translated vector
plot_vector_2d(ax, [0, 0], base_vector[:2], 'blue', 'Original Vector')  # From (0, 0) to (1, 1)
plot_vector_2d(ax, [4, 5], base_vector[:2], 'red', 'Transformed Vector')  # From (4, 5) to (5, 6)

# Add legend, grid, and labels
plt.legend()
plt.grid(True)
plt.title("Vector Transformations - Translation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()