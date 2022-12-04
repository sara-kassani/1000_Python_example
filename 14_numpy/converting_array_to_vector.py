row = np.r_['r', [1,2,3]]     # shape: (1, 3)
column = np.r_['c', [1,2,3]]  # shape: (3,1)


# Alternatively, you can reshape it to (1, n) for row, or (n, 1) for column

row = my_vector.reshape(1, -1)
column = my_vector.reshape(-1, 1)

# where the -1 automatically finds the value of n
