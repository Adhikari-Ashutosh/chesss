from pieces import *
from board import *
import random
class game:
    def __init__(self):
        self.board = Board()
        self.turn = 0
        self.update = True
       
    def make_moves(self,x,y,xn,yn):
        print("here")
        if self.board.board[x][y]!=None:
            print("here1")
            if self.board.board[x][y].color==self.turn:
                if self.board.make_moves(self.board.board[x][y],x,y,xn,yn):
                    self.turn=1-self.turn
                    self.update=True
                    self.turn=1-self.turn
                    print("here2")
                    return True
                else:
                    choice=self.board.getPieceList(self.turn)
                    #choose a random piece from choice
                    piece=random.choice(choice)
                    #get the moves of the piece
                    moves=self.board.allowed_moves(piece)
                    move=None
                    print("here3")
                    while len(moves)==0:
                    #choose a random move from moves
                        piece=random.choice(choice)
                        moves=self.board.allowed_moves(piece)
                    move=random.choice(moves)
                    #make the move
                    self.board.make_moves(piece,piece.x,piece.y,move[0],move[1])
                    
                    self.turn=1-self.turn
                    return False
            else:
                    choice=self.board.getPieceList(self.turn)
                    #choose a random piece from choice
                    piece=random.choice(choice)
                    #get the moves of the piece
                    moves=self.board.allowed_moves(piece)
                    move=None
                    while len(moves)==0:
                    #choose a random move from moves
                        piece=random.choice(choice)
                        moves=self.board.allowed_moves(piece)
                    move=random.choice(moves)
                    #make the move
                    self.board.make_moves(piece,piece.x,piece.y,move[0],move[1])
                    
                    self.turn=1-self.turn
                    print("here4")
                    return False
        else:
                    choice=self.board.getPieceList(self.turn)
                    #choose a random piece from choice
                    piece=random.choice(choice)
                    #get the moves of the piece
                    moves=self.board.allowed_moves(piece)
                    move=None
                    while len(moves)==0:
                    #choose a random move from moves
                        piece=random.choice(choice)
                        moves=self.board.allowed_moves(piece)
                    move=random.choice(moves)
                    #make the move
                    self.board.make_moves(piece,piece.x,piece.y,move[0],move[1])
                    print("here 5")
                    self.turn=1-self.turn
                    return False

        

    #score the board position
    def nattacked(self,piece):
        moves=piece.get_moves(self.board)
        count=0
        for move in moves:
            if self.board.board[move[0]][move[1]]!=None and self.board.board[move[0]][move[1]].color!=piece.color:
                count+=1
        return count
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
                            value += self.board.board[row][col].get_value()*col*0.1+self.nattacked(self.board.board[row][col])*0.2
                        elif color==1:
                            value+=self.board.board[row][col].get_value()*(6-col)*0.1+self.nattacked(self.board.board[row][col])*0.2
        return value
    #create function as a input for the neural network
    def get_input(self):
        input=[]
        for row in range(6):
            for col in range(6):
                if self.board.board[row][col]!=None:
                    if self.board.board[row][col].color==0:
                        input.append(ord(self.board.board[row][col].symbol))
                    elif self.board.board[row][col].color==1:
                        input.append(-ord(self.board.board[row][col].symbol))
                else:
                    input.append(0)
        input.append(self.turn)
        return input
