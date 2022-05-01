import os

def cls():
    os.system('clear')

class Squares:
    def __init__(self, chip = ' '):
        self.chip = chip
        self.row = '+---'
        self.column = ''

    def print_row(self):
        print(self.row, end='')

    def print_col(self):
        self.column = ('| ' + self.chip + ' ')
        print(self.column, end='')
    
    def change_chip(self, player):
        if player == player1:
            self.chip = 'x'
        if player == player2:
            self.chip = 'o'


class Grid:
    def __init__(self):
        self.square = []

        for column in range(6):
            self.square.append([])
            for row in range(7):
                grid_point1 = Squares(' ')
                self.square[column].append(grid_point1)
#prints grid each square is a point on the grid in square[row][column] format starting at the top left[0][0] square to bottom right[5][6]

    def grid(self):
        row=0
        print('  1   2   3   4   5   6   7')
        for grid in range(6):
            for row in range(7):
                self.square[grid][row].print_row()
                if row == 6:
                    print('+', end='')
            print()

            for col in range(7):
                self.square[grid][col].print_col()
                if col ==6:
                    print('|', end='')
            print()
        print('+---' *7 + '+')
            

    def populate_square(self, user_input, player):
        x=5
        for row in range(6):
            if self.square[x][user_input].chip ==' ':
                self.square[x][user_input].change_chip(player)
                break
            x-=1

    def did_i_win(self, player):
        if player == 'player1':
            token = 'x'
        else:
            token = 'o'
        
        def check_horizontal():
            for row in range(6):
                count = 0
                for column in range(7):
                    if token == self.square[row][column].chip:
                        count+=1
                    else:
                        count = 0
                    if count == 4:
                        return True
        
        def check_vertical():
            for column in range(7):
                count = 0
                for row in range(6):
                    if token == self.square[row][column].chip:
                        count+=1
                    else:
                        count = 0
                    if count == 4:
                        return True
        
        def check_diagnal_1():
            start_past_column_0 = 6
            new_start_column=1
            new_start_column_counter=1
            for row in range(13):
                new_row=5
                count = 0
                if row >0 and row <= 6:
                    for x in range(row):                
                        row-=1
                        if token == self.square[row][x].chip:
                            count+=1
                        else:
                            count = 0

                        if count == 4:
                            return True 
                elif row > 6:
                    for y in range(start_past_column_0):
                        if token == self.square[new_row][new_start_column_counter].chip:
                            count+=1
                        else:
                            count = 0

                        if count == 4:
                            return True
                        new_row-=1
                        new_start_column_counter+=1
                    start_past_column_0-=1
                    new_start_column+=1
                    new_start_column_counter=new_start_column
                
        def check_diagnal_2():
            start_past_column_0 = 6
            new_start_column=1
            new_start_column_counter=1
            row = 5
            for x in range(13):
                count = 0
                if x >0 and x <=6:
                    start_row=row
                    for y in range(x):
                        if token == self.square[start_row][y].chip:
                            count+=1
                        else:
                            count = 0

                        if count == 4:
                            return True
                        start_row+=1
                    row-=1

                elif x>6:
                    start_row = 0
                    for y in range(start_past_column_0):
                        if token == self.square[start_row][new_start_column_counter].chip:
                            count+=1
                        else:
                            count = 0

                        if count == 4:
                            return True
                        start_row+=1
                        new_start_column_counter+=1
                    row-=1
                    start_past_column_0-=1
                    new_start_column+=1
                    new_start_column_counter=new_start_column

        if check_horizontal() == True or check_vertical() == True or check_diagnal_1() == True or check_diagnal_2() == True:
            return True
        else:
            return False

        

                

print('Welcome to connect4!')
player1 = input('Player 1 please enter your name ')
player2 = input('Player 2 please enter your name ')
cls()
print(player1, ' you will be in control of the x tokens ', player2, ' you will be in control of the o tokens here is your blank board. Good luck!!\n\n')
game = Grid()
game.grid()
for x in range(22):
    if x < 21:
        winner = False
        if winner == False:
            player1_move = input('\n\n' + player1 + ' please choose the column you would like to place your token in ')
            game.populate_square(int(player1_move)-1, player1)
            game.grid()
            winner = game.did_i_win('player1')
            if winner == True:
                print(player1, ' Wins!!!!!')
                break

            player2_move = input('\n\n' + player2 + ' please choose the column you would like to place your token in ')
            game.populate_square(int(player2_move)-1, player2)
            game.grid()
            winner = game.did_i_win('player2')
            if winner == True:
                print(player2, ' Wins!!!!!')
                break
    else:
        print('Its a tie :(')
        break
    cls()
    game.grid()

