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
    
    def change_chip(self, player):
        if player == player1:
            self.chip = 'x'
        if player == player2:
            self.chip = 'o'


class Grid:
    def __init__(self):
        self.square = []

        for row in range(7):
            self.square.append([])
            for column in range(7):
                grid_point1 = Squares(' ')
                self.square[row].append(grid_point1)
#prints grid each square is a point on the grid in square[column][row] format starting at the top left[0][0] square to bottom right[6][5]
    def grid(self):
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

    def populate_square(self, user_input, player):
        x=5
        for row in range(6):
            if self.square[user_input][x].chip ==' ':
                self.square[user_input][x].change_chip(player)
                break
            x-=1

    def did_i_win(self, player):
        count = 0
        if player == 'player1':
            token = 'x'
        else:
            token = 'o'

        for column in range(6):
            for row in range(7):
                if token == self.square[column][row].chip:
                    count+=1
                else:
                    count = 0
                if count == 4:
                    return True
        
        for row in range(7):
            for column in range(6):
                if token == self.square[column][row].chip:
                    count+=1
                else:
                    count = 0
                if count == 4:
                    return True
        for check in range(7):
            if check is >= 3:
                column = 0
            else:
                column = check
            for y in range(6):

        return False

        

                

print('Welcome to connect4!')
player1 = input('Player 1 please enter your name ')
player2 = input('Player 2 please enter your name ')
print(player1, ' you will be in control of the x tokens ', player2, ' you will be in control of the o tokens here is your blank board. Good luck!!\n\n')
game = Grid()
game.grid()
for x in range(22):
    if x < 21:
        winner = False
        if winner == False:
            player1_move = input('\n\n' + player1 + ' please choose the column you would like to place your token in ')
            game.populate_square(int(player1_move), player1)
            game.grid()
            winner = game.did_i_win('player1')
            if winner == True:
                print(player1, ' Wins!!!!!')
                break

            player2_move = input('\n\n' + player2 + ' please choose the column you would like to place your token in ')
            game.populate_square(int(player2_move), player2)
            game.grid()
            winner = game.did_i_win('player2')
            if winner == True:
                print(player2, ' Wins!!!!!')
                break
    else:
        print('Its a tie :(')
        break

