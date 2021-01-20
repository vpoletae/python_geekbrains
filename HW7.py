#1
class Matrix(object):

    def __init__(self, lists: list):
        if len(lists) == 0:
            raise ValueError("Matrix can not be empty!")
        row_len = len(lists[0])
        for row in lists:
            if len(row) == row_len:
                pass
            else:
                raise ValueError("All rows in matrix must be of the same size!")
        self.lists = lists

    def __str__(self):
        matrix = ''
        for row in self.lists:
            row_str = ' '.join([str(elem) for elem in row]) + '\n'
            matrix += row_str
        matrix = matrix.rstrip()
        return matrix

    def __add__(self, other):
        assert len(self.lists) == len(other.lists), "Matrices must be of the same size!"
        assert len(self.lists[0]) == len(other.lists[0]), "Matrices must be of the same size!"
        lists = []
        rows = len(self.lists)
        el_in_row = len(self.lists[0])
        for row_i in range(rows):
            new_row = []
            for el_i in range(el_in_row):
                new_row.append(self.lists[row_i][el_i] + other.lists[row_i][el_i])
            lists.append(new_row)
        return Matrix(lists)

try:
    matrix_0 = Matrix([[2,2], [2,2,3]])
    print(matrix_0)
except ValueError as e:
    print(e)
print('-' * 40)
matrix_1 = Matrix([[2,2], [2,2]])
print(matrix_1)
print('-' * 40)
matrix_2 = Matrix([[3,3], [3,3]])
matrix_3 = Matrix([[1,1], [1,1]])
matrix_sum = matrix_1 + matrix_2 + matrix_3
print(matrix_sum)

#2
# Not completely understand how parameter (H/V) should be handled
class Clothes(object):

    def __init__(self, ctype, param): # clothes type
        self.ctype = ctype.lower()
        self.param = param

    @property
    def cloth_required(self):
        if self.ctype == 'coat':
            return round(self.param/6.5 + 0.5, 2)
        elif self.ctype == 'suit':
            return round(2 * self.param + 0.3, 2)
        else:
            raise ValueError('Clothes type is unknown! Please create "coat" or "suit"')

coat = Clothes('Coat', 10)
print(coat.cloth_required)

suit = Clothes('Suit', 20)
print(suit.cloth_required)

#3
class Cell(object):

    def __init__(self, amount):
        assert amount > 0, 'Cell can not be negative number or 0!'
        self.amount = amount

    def __add__(self, other):
        return Cell(int(self.amount + other.amount))

    def __sub__(self, other):
        assert self.amount > other.amount, 'Result of substraction can not be negative!'
        return Cell(int(self.amount - other.amount))

    def __mul__(self, other):
        return Cell(int(self.amount * other.amount))

    def __truediv__(self, other):
        return Cell(int(self.amount / other.amount))

    def make_order(self, cells_in_row):
        complete_rows = self.amount // cells_in_row
        odd_cells = self.amount % cells_in_row
        cells = ''
        for _ in range(complete_rows):
            cells += '*' * cells_in_row
            cells += '\n'
        cells += '*' * odd_cells
        return cells

    def __str__(self):
        return str(self.amount)

cell_1 = Cell(100)
cell_2 = Cell(5)
cell_3 = Cell(2)

cell_sum = cell_1 + cell_2 + cell_3
print(cell_sum)
cell_sub = cell_1 - cell_2 - cell_3
print(cell_sub)
cell_mul = cell_1 * cell_2 * cell_3
print(cell_mul)
cell_div = cell_1 / cell_2 / cell_3
print(cell_div)

print(Cell(-1))
print(cell_3 - cell_2)

print(cell_1.make_order(20))
print(cell_2.make_order(2))