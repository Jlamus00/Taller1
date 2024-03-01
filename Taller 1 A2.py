
import numpy as np

# Initialize matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Sum of matrices
sum_matrix = A + B
print("Sum of matrices: \n", sum_matrix)

# Difference of matrices
diff_matrix = A - B
print("Difference of matrices: \n", diff_matrix)

# Scalar multiplication
scalar = 20.2
scalar_A = scalar * A
print("Scalar multiplication: \n", scalar_A)

# Matrix multiplication
product_matrix = np.matmul(A, B)
print("Matrix multiplication: \n", product_matrix)

# Producto punto
dot_product = np.einsum('ij,ij->i', A, B)
print("Producto punto: \n", dot_product)