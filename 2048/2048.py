import random

class Board:
    def __init__(self):
        print("Commands are as follows : \n'W' or 'w' : Move Up\n'S' or 's' : Move Down\n'A' or 'a' : Move Left\n'D' or 'd' : Move Right")
        self.board = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.add_number()
        self.print_board()
        
    def print_board(self):
        print('\n'.join(map(str, self.board)))
    
    def add_number(self):
        empty_spaces = []

        for index_row,row in enumerate(self.board):
            for index_space,space in enumerate(row):
                if space == 0:
                    empty_spaces.append((index_row,index_space))
        
        if len(empty_spaces) > 0:
            posizione_y,posizione_x = random.choice(empty_spaces)
            self.board[posizione_y][posizione_x] = 2


board = Board()