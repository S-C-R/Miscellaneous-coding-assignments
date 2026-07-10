import numpy as np

class Board:

    def __init__(self, board_set = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]):
        self.board_state = board_set #' ' is an empty space
        self.player = 'X'
        self.x_view = self.board_state
        self.o_view = self.board_state

    def __str__(self):
        return f" Board             X                   O \n {self.board_state[0]} {self.x_view[0]} {self.o_view[0]}\n {self.board_state[1]} {self.x_view[1]} {self.o_view[1]}\n {self.board_state[2]} {self.x_view[2]} {self.o_view[2]}\n"

    def illegal_move(self,x,y):
        if self.board_state[x][y] == ' ':
            return False
        return True

    def winn(self):
        for row in (0, 1, 2):
            if self.board_state[row][0] != ' ' and self.board_state[row][0] == self.board_state[row][1] == self.board_state[row][2]:
                return True
        for col in (0, 1, 2):
            if self.board_state[0][col] != ' ' and self.board_state[0][col] == self.board_state[1][col] == self.board_state[2][col]:
                return True
        if self.board_state[0][0] != ' ' and self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2]:
                return True
        if self.board_state[0][2] != ' ' and self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0]:
                return True
        return False
        
    def get_x_view(self):
        return self.x_view
        
    def get_o_view(self):
        return self.o_view
        
    def game_over(self):
        if self.winn():
            if self.player == 'X':
                self.winner = 'O'
            else:
                self.winner = 'X'
            return True
        for i in (0, 1, 2):
            for j in (0, 1, 2):
                if self.board_state[i][j] == ' ':
                    return False
        print("It\'s a draw")
        return True
        
    def add_move(self,x,y):
        if not self.illegal_move(x,y):
            self.board_state[x][y] = self.player
            if self.player == 'X':
                self.x_view = self.board_state
                self.player = 'O'
            else:
                self.o_view = self.board_state
                self.player = 'X'
        else:
            if self.player == 'X':
                self.x_view = self.board_state
                self.player = 'O'
            else:
                self.o_view = self.board_state
                self.player = 'X'
