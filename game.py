from pieces import *
from board import *
class game:
    def __init__(self):
        self.board = Board()
        self.turn = 0
        self.update = True
    def make_moves(self,x,y,xn,yn):
        self.turn=1-self.turn
        return self.board.make_moves(self.board,self.board.get_piece(x,y),xn,yn)
    #score the board position
    def nattacked(self,piece):
        moves=piece.get_moves(self.board.board)
        count=0
        for move in moves:
            if self.board.board[move[0]][move[1]]!=None and self.board.board[move[0]][move[1]].color!=piece.color:
                count+=1
    def CheckResult(self):
        if self.board.is_checkmate(0):
            return 1
        elif self.board.is_checkmate(1):
            return -1
        elif self.board.is_draw():
            return 2
        else:
            return 0
    def score(self, color):
        value = 0
        for row in range(6):
            for col in range(6):
                if self.board.board[row][col] != None:
                    if self.board.board[row][col].get_color() == color:
                        if color==0:
                            value += self.board.board[row][col].get_value()*col+self.nattacked(self.board.board[row][col])*2
                        elif color==1:
                            value+=self.board.board[row][col].get_value()*(6-col)+self.nattacked(self.board.board[row][col])*2
        return value
    #create function as a input for the neural network
    def get_input(self):
        input=[]
        for row in range(6):
            for col in range(6):
                if self.board.board[row][col]!=None:
                    if self.board.board[row][col].color==0:
                        input.append(int(self.board.board[row][col].get_symbol()))
                    elif self.board.board[row][col].color==1:
                        input.append(-int(self.board.board[row][col].get_symbol()))
                else:
                    input.append(0)
        return input

    
                
    

