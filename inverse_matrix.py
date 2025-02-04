def inverse_matrix(matrix):
    #check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Input matrix must be square for inversion.")
    #augment the matrix with the identity matrix
    n = len(matrix)
    #initialize an empty identity matrix
    identity = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identity.append(row)

    #augment the original matrix with the identity matrix
    augmented_matrix = []
    for i, row in enumerate(matrix):
        augmented_row = row + identity[i]
        augmented_matrix.append(augmented_row)

    for i in range(n):
        #find the pivot row
        #manzoram az pivot row hamoon satre matrise hamaniye!!
        column_values = []
        for k in range(i, n):
            absolute_value = abs(augmented_matrix[k][i])
            #the abs function is just for getting the absolute value of a number!
            column_values.append(absolute_value)

        max_index = i + column_values.index(max(column_values))
        pivot_row = max_index
        #swap the current row with the pivot row
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        #scale the pivot row to have a leading 1
        pivot_value = augmented_matrix[i][i]
        augmented_matrix[i] = [x / pivot_value for x in augmented_matrix[i]]
        #eliminate other rows

        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                # store the original row to be modified
                original_row = augmented_matrix[j][:]
                # perform the row operation
                for k, x in enumerate(augmented_matrix[j]):
                    augmented_matrix[j][k] = x - factor * augmented_matrix[i][k]

    #extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix

#example usage with a 3x3 matrix:
input_matrix = [
    [1, 3, 4],
    [0, 1, 2],
    [0, 1, 3]
]
result = inverse_matrix(input_matrix)
if result is not None:
    import numpy as np
    print("Original matrix:")
    print(np.array(input_matrix))
    print("\nInverse matrix:")
    print(np.array(result))
    #I used numpy, just to show the array! nothing else!!
import time
time.sleep(30)
