"""
Complete the matrix_addition() function that takes two nested lists, representing 2 matrices, as parameters. If the 2 parameter matrices can be added, i.e.,  matrix1 and matrix2 have the
same dimensions, the function returns a new nested list representing the sum of these matrices. Otherwise, the function prints "Incorrect Dimensions!" and returns -1.
"""

def matrix_addition(matrix1, matrix2):
    if (
        len(matrix1) == len(matrix2)
        and len(matrix1[0]) == len(matrix2[0])
    ):
        added_matrix = []
        
        for y in range(len(matrix1)):
            new_row = [] 
            for x in range(len(matrix1[y])):
                new_row.append(matrix1[y][x] + matrix2[y][x])
                
            added_matrix.append(new_row)
                    
        return added_matrix
        
    else:
        print("Incorrect Dimensions!")
        return -1

matrix1 = [[11, 3], [7, 11]]
matrix2 = [[5, 1], [0, 2]]
result = matrix_addition(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} + {matrix2} = {result}")
print()

matrix1 = [[11, 3], [7, 11]]
matrix2 = [[5, 1], [0, 2], [-1, -7]]
result = matrix_addition(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} + {matrix2} = {result}")
print()
