class Squares:
    def __init__(self, chip = ' '):
        self.chip = chip
        self.column = '+---'
        self.row = ''
        #print(self.column, '\n', self.row)

    def print_col(self):
        print(self.column, end='')

    def print_row(self):
        self.row = ('| ' + self.chip + ' ')
        print(self.row, end='')
    
    def change_chip(self):
        self.chip = 'x'


class Grid:
    def __init__(self):
        self.square = []

        for row in range(7):
            self.square.append([])
            for column in range(7):
                grid_point1 = Squares('o')
                self.square[row].append(grid_point1)

    def grid(self):
        self.square[0][0].change_chip()
        self.square[0][1].change_chip()
        self.square[0][2].change_chip()
        # self.square[0][3].change_chip()
        # self.square[0][4].change_chip()
        # self.square[0][5].change_chip()
        # self.square[0][6].change_chip()
        # self.square[1][0].change_chip()
        # self.square[1][1].change_chip()
        # self.square[1][2].change_chip()
        # self.square[1][3].change_chip()
        # self.square[1][4].change_chip()
        # self.square[1][5].change_chip()
        # self.square[1][6].change_chip()
        # self.square[2][0].change_chip()
        # self.square[2][1].change_chip()
        # self.square[2][2].change_chip()
        # self.square[2][3].change_chip()
        # self.square[2][4].change_chip()
        # self.square[2][5].change_chip()
        # self.square[2][6].change_chip()
        # self.square[3][0].change_chip()
        # self.square[3][1].change_chip()
        # self.square[3][2].change_chip()
        # self.square[3][3].change_chip()
        # self.square[3][4].change_chip()
        # self.square[3][5].change_chip()
        # self.square[3][6].change_chip()
        # self.square[4][0].change_chip()
        # self.square[4][1].change_chip()
        # self.square[4][2].change_chip()
        # self.square[4][3].change_chip()
        # self.square[4][4].change_chip()
        # self.square[4][5].change_chip()
        # self.square[4][6].change_chip()
        # self.square[5][0].change_chip()
        # self.square[5][1].change_chip()
        # self.square[5][2].change_chip()
        # self.square[5][3].change_chip()
        # self.square[5][4].change_chip()
        # self.square[5][5].change_chip()
        # self.square[5][6].change_chip()
        # self.square[6][0].change_chip()
        # self.square[6][1].change_chip()
        # self.square[6][2].change_chip()
        # self.square[6][3].change_chip()
        # self.square[6][4].change_chip()
        # self.square[6][5].change_chip()
        # self.square[6][6].change_chip()
        row=0


        for grid in range(6):
            print()
            for col in range(7):
                self.square[row][col].print_col()
                if col == 6:
                    print('+', end='')
            print()
            for row in range(7):
                #print(row, grid)
                self.square[row][grid].print_row()
                if row ==(6):
                    print('|', end='')
            if grid == 5:
                print()
                print('+---' *7 + '+')

game = Grid()
game.grid()
# first_square = Squares()
# second_square = Squares('x')