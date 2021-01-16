from Utilities.Switch import Switch
from Services.Models.MatrixModels import *
from Services.MyMath.Algebra import MatrixSolver
from Services.MyMath import FunctionSolver

class FunctionalitySwitch(Switch):
    def Factorial(self, num: int):
        return FunctionSolver.Factorial(num)

    def TransposeMatrix(self, matrix):
        return MatrixSolver.TransposeMatrix(matrix)

    def IdentityMatrix(self, n: int):
        return MatrixSolver.IdentityMatrix(n)

    def ZeroMatrix(self, dimension: MatrixDimension):
        return MatrixSolver.ZeroMatrix(dimension)

    def SumMatrix(self, matrix1, matrix2):
        return MatrixSolver.SumMatrix(matrix1, matrix2)

    def ProdMatrix(self, matrix1, matrix2):
        return MatrixSolver.ProdMatrix(matrix1, matrix2)