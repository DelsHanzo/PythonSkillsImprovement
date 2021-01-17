from Services.Models import FunctionalityEnum
from Services.Models.MatrixModels import MatrixDimension
from FunctionalitySwitch import FunctionalitySwitch
from Services.MyMath.FunctionSolver import *
from Utilities import Printer
from Services.Models.FunctionalityEnum import Functionality

def Main():
    StartDemo()

def StartDemo():
    switch = FunctionalitySwitch(Functionality)

    number = 5
    
    print(Functionality.Factorial.name)
    print(switch(Functionality.Factorial)(number))

    Printer.SepareteContext()

    print(Functionality.IdentityMatrix.name)
    Printer.PrintMatrix(switch(Functionality.IdentityMatrix)(number))

    Printer.SepareteContext()

    print(Functionality.ZeroMatrix.name)
    Printer.PrintMatrix(switch(Functionality.ZeroMatrix)(MatrixDimension(number, number -1)))

    Printer.SepareteContext()

    m1 = [[1, 0], [1,-1]] 

    print(Functionality.TransposeMatrix.name)
    Printer.PrintMatrix(switch(Functionality.TransposeMatrix)(m1))

    Printer.SepareteContext()

    m2 = [[1, 2], [2, 4]] 

    print(Functionality.SumMatrix.name)
    Printer.PrintMatrix(switch(Functionality.SumMatrix)(m1, m2))

    Printer.SepareteContext()

    print(Functionality.ProdMatrix.name)
    Printer.PrintMatrix(switch(Functionality.ProdMatrix)(m1, m2))    

print("Python skills and MathMagic\n")
Main()