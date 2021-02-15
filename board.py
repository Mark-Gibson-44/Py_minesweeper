import random


class Board:

    def __init__(self):
        self.height = 10#Height of board
        self.width = 10#width of Board
        self.board = self.gen_board()#Variable denoting whole board
        self.mine_number = 18#Number of Mines on a given Board
        self.mine_locations = []#List of Tuples consisting of mine locations
        self.selected = []#list of areas the have been selected
    def gen_board(self):
        board = []
        for i in range(self.height):
            board.append([])
            for j in range(self.width):
                board[i].append(' ')
        return board
    def gen_mines(self):
        for i in range (self.mine_number):
            rand_col = random.randint(0, self.width-1)
            rand_row = random.randint(0, self.height-1)
            self.mine_locations.append((rand_col, rand_row))
            self.board[rand_col][rand_row] = 'X'

    def display(self):
        for rows in self.board:
            print(rows)
    def is_mine(self, x, y):
        return self.board[x][y] == 'X'
    def count_surrounding(self, x,y ):
        mines_around = 0
        for i in range(3):
            for j in range(3):
                if((i-1 == 0 and j-1 == 0) or (x+(i-1) >= self.width) or (y+(j-1) >= self.height) or (x+(i-1) < 0) or (y+(j-1) < 0)):
                    continue
                if(self.is_mine(x+(i-1),y+(j-1))):
                    mines_around = mines_around + 1
        return mines_around
    def log_mines(self):
        for i in range (self.height):
            for j in range(self.width):
                print("Position (", i, ",", j, ") has ", self.count_surrounding(i,j))
    def set_all_points(self):
        for i in range (self.height):
            for j in range(self.width):
                self.board[i][j] = self.count_surrounding(i,j)
    
    def play(self):
        print("Input a coordinate to check")
        x = input()
        y = input()
        #print(type(x),type(y))
        print(self.count_surrounding(int(x),int(y)))
    def show_mine_loc(self):
        for mines in self.mine_locations:
            print(mines)



b = Board()
b.gen_mines()
b.display()
b.show_mine_loc()

#b.set_all_points()


