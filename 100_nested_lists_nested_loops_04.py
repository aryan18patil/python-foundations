"""
Complete the matrix_transposition() function that takes a single nested list of integers representing a matrix called matrix as a parameter. The function creates and returns a new nested
list representing the transpose of the parameter matrix.
"""

def matrix_transposition(matrix):
    transpose_matrix = []
    
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if y == 0:
                transpose_matrix.append([matrix[y][x]])
                
            else:
                transpose_matrix[x].append(matrix[y][x])
                
    return transpose_matrix

matrix = [[1, 2],[3, 4],[5, 6]]
transpose_matrix = matrix_transposition(matrix)
print("Transpose matrix:", transpose_matrix)
print()

matrix = [[1, -2]]
transpose_matrix = matrix_transposition(matrix)
print("Transpose matrix:", transpose_matrix)
print()
