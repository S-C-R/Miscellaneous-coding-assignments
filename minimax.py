from board import Board


class Minimax:
    def __init__(self,game):
        self.boardgame = game
    
    def is_terminal(self):
        if self.boardgame.winner != None:
            return True
        return False

    def get_utility():
        if self.boardgame.winner == 'X':
            return 1
        elif self.boardgame.winner == 'O':
            return -1
        else:
            return 0
            
    def is_X(self,game):
        if game.player == 'X':
            return True
        return False

    def get_children(self,node):
        return
        
    def best_play(self):
        best = float('-inf')
        best_move = None
        for move in self.boardgame:
            if move > best:
                best_move = move
        return best_move
function prestige() {
    prestigelevel = Math.log(movement);
    rotateAngle = 0;
    movement = 0;
    bonusmovement = 15;
    bonusrotation = 15;
    verticalspeed = 45;
    verticalposition = -15;
    randomtime = 20;
    maxdepth = 0;
    rotationstored = 0;
    totalrotations = 0;
    rotationprice = 2;
  }