import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Operator
from qiskit.circuit.library import HGate

# Create a Hadamard gate and get its matrix representation
gate = HGate()
gate_matrix = Operator(gate).data
# Map the real and imaginary parts of the matrix to colors
real_colors = plt.get_cmap('Reds')(np.real(gate_matrix) / np.max(np.real(gate_matrix)))
epsilon = 1e-10  # Small constant to avoid division by zero
imag_colors = plt.get_cmap('Blues')(np.imag(gate_matrix) / (np.max(np.imag(gate_matrix)) + epsilon))


# Combine the color mappings to create a color-coded matrix
color_matrix = np.zeros((2, 2, 4))
color_matrix[..., :3] = real_colors[..., :3] + imag_colors[..., :3]
color_matrix[..., 3] = 1  # Set alpha channel to 1

# Normalize the color matrix to the range [0, 1]
color_matrix[..., :3] /= np.max(color_matrix[..., :3])

# Plot the color-coded matrix
plt.imshow(color_matrix, interpolation='nearest')
plt.show()
