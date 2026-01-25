def mulScalar(matrix, scale):
    for row in matrix: # [[1, 2], [3, 4]] --> [1, 2], [3, 4]
        for i in range(len(row)): # [1, 2], [3, 4] --> [2, 4], [6, 8]
            row[i] *= scale
    return matrix
    ## return [[num * scale for num in row] for row in matrix] # alternative

def addMatrices(mat1, mat2):
    pass # wait

matrix = [[6, 7], [8, 9]]
print('Original: {}'.format(matrix))
print('New: {}'.format(mulScalar(matrix, 3)))