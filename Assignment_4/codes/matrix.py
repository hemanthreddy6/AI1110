import numpy as np

# Formatting the print options
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

# Initializing the matrix
A = np.array([[5/6,1/6,0,0],
              [0,5/6,1/6,0],
              [0,0,5/6,1/6],
              [0,0,0,5/6],
             ])
          
# Getting A^2
B = np.linalg.matrix_power(A, 2)
print(B)
print("------------------------------")

# Getting A^3
B = np.linalg.matrix_power(A,3)
print(B)
