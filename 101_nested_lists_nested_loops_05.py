"""
Complete the matrix_multiplication() function that takes two nested lists, representing 2 matrices, as parameters. If the 2 parameter matrices can be multiplied, i.e., the number of
columns in matrix1 is equal to the number of rows in matrix2, the function returns a new nested list representing the product of these matrices. Otherwise, the function prints "Incorrect
Dimensions!" and returns -1.
"""

def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        print("Incorrect Dimensions!")
        return -1
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            row.append(0)
        result.append(row)
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    return result

matrix1 = [[11, 3], [7, 11]]
matrix2 = [[8, 0, 1],[0, 3, 5]]
result = matrix_multiplication(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} * {matrix2} = {result}")
print()

matrix1 = [[2, 3], [0, -1]]
matrix2 = [[1, 3]]
result = matrix_multiplication(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} * {matrix2} = {result}")
print()
