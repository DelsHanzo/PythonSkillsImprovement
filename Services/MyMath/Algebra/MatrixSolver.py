from Services.Models.MatrixModels import *

def TransposeMatrix(matrix):
    return map(list, zip(*matrix))

def IdentityMatrix(n: int):
    return [[int(column==row) for column in range(n)] for row in range(n)]

def IsSquaredMatrix(matrix):
    return all (len (row) == len (matrix) for row in matrix)

def ZeroMatrix(dimension: MatrixDimension):
    return [[0 for x in range(dimension.columns)] for y in range(dimension.rows)]

def SumMatrix(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def ProdMatrix(matrix1, matrix2):
    # ##Alternative algorithm:
    # # iterating rows of X matrix
    # for i in range( len(X) ):
    # # iterating columns of Y matrix
    #     for j in range(len(Y[0])):
    #     # iterating rows of Y matrix
    #         for k in range(len(Y)):
    #             result[i][j] += X[i][k] * Y[k][j]
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1] 
