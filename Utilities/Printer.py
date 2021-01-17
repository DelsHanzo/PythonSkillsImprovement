def PrintDictionary(dictionary: dict, separator: str = "\n"):
   [print(key, value) for key, value in dictionary.items()] 

def PrintMatrix(matrix):
   for r in matrix:
      print(r)

def SepareteContext(nBackSpaces: int = 1):
   for i in range(nBackSpaces):
      print("")
