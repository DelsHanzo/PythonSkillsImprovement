class MatrixCell:
    rowIndex: int
    columnIndex: int

    def __init__(self, row, column):
        self.rowIndex = row
        self.columnIndex = column

class MatrixDimension:
    rows: int
    columns: int

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
