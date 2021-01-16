from Services.Models.MatrixModels import MatrixDimension
from FunctionalitySwitch import FunctionalitySwitch
from Services.MyMath.FunctionSolver import *
from Utilities.Helpers.EnumHelper import *
from Utilities import Printer
from Services.Models.FunctionalityEnum import Functionality

def Main():
    StartDemo()

def StartDemo():
    switch = FunctionalitySwitch(Functionality)

    number = 5
    
    print(switch(Functionality.Factorial)(number))
    Printer.PrintMatrix(switch(Functionality.IdentityMatrix)(number))
    Printer.PrintMatrix(switch(Functionality.ZeroMatrix)(MatrixDimension(number, number -1)))

    m1 = [[1, 0], [1,-1]] 
    Printer.PrintMatrix(switch(Functionality.TransposeMatrix)(m1))

    m2 = [[1, 2], [2, 4]] 
    Printer.PrintMatrix(switch(Functionality.SumMatrix)(m1, m2))
    Printer.PrintMatrix(switch(Functionality.ProdMatrix)(m1, m2))

print("Python skills and MathMagic\n")
Main()