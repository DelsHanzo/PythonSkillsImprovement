import enum

"""Get list that contains all enum values
"""
def GetEnumNames(EnumType: enum.Enum):
   return [e.name for e in EnumType]
