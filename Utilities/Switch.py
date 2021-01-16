from enum import Enum

class Switch:
    def __init__(self, enum: Enum):
        self.__enum = enum
        if hasattr(self, "default"):
            return

    def __call__(self, value: Enum):
        if not isinstance(value, self.__enum):
            raise ValueError(f"Invalid value: {value}")
        if hasattr(self, value.name):
            return getattr(self, value.name)
        else:
            return self.default()