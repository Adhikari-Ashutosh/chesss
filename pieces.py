

#define the king piece on a chess board
#DEFINED 0 AS WHITE AND 1 AS BLACK
#import deepcopy
import copy
from pieces.King import *
class piece:
    def __init__(self,color,x,y):
        self.color=color
        self.x=x
        self.y=y
        self.symbol=""
        self.value=-1

    def __str__(self):
        return  str(self.symbol)+str(self.color)
    def __repr__(self):
        return  str(self.symbol)+str(self.color)
    def __eq__(self, other):
        if other==None:
            return False
        return self.color == other.color and self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash((self.color, self.name))
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def get_symbol(self):
        return self.symbol+str(self.color)
    def capture(self,other):
        if self.color != other.color:
            return True
        return False

class king(piece):
    def __init__(self):
        self.symbol="K"
        self.value=0
        self.name="king"
    def get_moves(self,board):
        #Check if the king can move up,down,right,left,up-right,up-left,down-right,down-left
        move_set=[]
        #up
        if self.y-1>-1:
            if board[self.x][self.y-1]==None:
                move_set.append((self.x,self.y-1))
            else:
                if self.capture(board[self.x][self.y-1]):
                    move_set.append((self.x,self.y-1))
        #down
        if self.y+1<5:
            if board[self.x][self.y+1]==None:
                move_set.append((self.x,self.y+1))
            else:
                if self.capture(board[self.x][self.y+1]):
                    move_set.append((self.x,self.y+1))
        #left
        if self.x-1>-1:
            if board[self.x-1][self.y]==None:
                move_set.append((self.x-1,self.y))
            else:
                if self.capture(board[self.x-1][self.y]):
                    move_set.append((self.x-1,self.y))
        #right
        if self.x+1<5:
            if board[self.x+1][self.y]==None:
                move_set.append((self.x+1,self.y))
            else:
                if self.capture(board[self.x+1][self.y]):
                    move_set.append((self.x+1,self.y))
        #up-left
        if self.x-1>-1 and self.y-1>-1:
            if board[self.x-1][self.y-1]==None:
                move_set.append((self.x-1,self.y-1))
            else:
                if self.capture(board[self.x-1][self.y-1]):
                    move_set.append((self.x-1,self.y-1))
        #up-right
        if self.x+1<5 and self.y-1>-1:
            if board[self.x+1][self.y-1]==None:
                move_set.append((self.x+1,self.y-1))
            else:
                if self.capture(board[self.x+1][self.y-1]):
                    move_set.append((self.x+1,self.y-1))
        #down-left
        if self.x-1>-1 and self.y+1<5:
            if board[self.x-1][self.y+1]==None:
                move_set.append((self.x-1,self.y+1))
            else:
                if self.capture(board[self.x-1][self.y+1]):
                    move_set.append((self.x-1,self.y+1))
        
        #down-right
        if self.x+1<5 and self.y+1<5:
            if board[self.x+1][self.y+1]==None:
                move_set.append((self.x+1,self.y+1))
            else:
                if self.capture(board[self.x+1][self.y+1]):
                    move_set.append((self.x+1,self.y+1))
        return move_set
        

class rook(piece):
    def __init__(self):
        self.symbol="R"
        self.value=5
        self.name="rook"
    def get_moves(self,board):
                moves = []
            #check if the rook can move left
                for i in range(self.x - 1, -1, -1):
                    if board[i][self.y] == None:
                        moves.append((i, self.y))
                    elif board[i][self.y].get_color() != self.color:
                        moves.append((i, self.y))
                        break
                    else:
                        break
                #check if the rook can move right
                for i in range(self.x + 1, 6):
                    if board[i][self.y] == None:
                        moves.append((i, self.y))
                    elif board[i][self.y].get_color() != self.color:
                        moves.append((i, self.y))
                        break
                    else:
                        break
                #check if the rook can move up
                for i in range(self.y - 1, -1, -1):
                    if board[self.x][i] == None:
                        moves.append((self.x, i))
                    elif board[self.x][i].get_color() != self.color:
                        moves.append((self.x, i))
                        break
                    else:
                        break
                #check if the rook can move down
                for i in range(self.y + 1, 6):
                    if board[self.x][i] == None:
                        moves.append((self.x, i))
                    elif board[self.x][i].get_color() != self.color:
                        moves.append((self.x, i))
                        break
                    else:
                        break
                return moves


class bishop(piece):
    def __init__(self):
        self.symbol="B"
        self.value=3
        self.name="bishop"
    def get_moves(self,board):
        moves = []
        #check if the bishop can move up and left
        i = self.x - 1
        j = self.y - 1
        while i > -1 and j > -1:
            if board[i][j] == None:
                moves.append((i, j))
            elif board[i][j].get_color() != self.color:
                moves.append((i, j))
                break
            else:
                break
            i -= 1
            j -= 1
        #check if the bishop can move up and right
        i = self.x - 1
        j = self.y + 1
        while i > -1 and j < 6:
            if board[i][j] == None:
                moves.append((i, j))
            elif board[i][j].get_color() != self.color:
                moves.append((i, j))
                break
            else:
                break
            i -= 1
            j += 1
        #check if the bishop can move down and left
        i = self.x + 1
        j = self.y - 1
        while i < 6 and j > -1:
            if board[i][j] == None:
                moves.append((i, j))
            elif board[i][j].get_color() != self.color:
                moves.append((i, j))
                break
            else:
                break
            i += 1
            j -= 1
        #check if the bishop can move down and right
        i = self.x + 1
        j = self.y + 1
        while i < 6 and j < 6:
            if board[i][j] == None:
                moves.append((i, j))
            elif board[i][j].get_color() != self.color:
                moves.append((i, j))
                break
            else:
                break
            i += 1
            j += 1
        return moves


class knight(piece):
    def __init__(self):
        self.symbol="N"
        self.value=3
        self.name="knight"
    def get_moves(self,board):
        moves = []
        #check if the knight can move up and left
        if self.x - 2 > -1 and self.y - 1 > -1:
            if board[self.x - 2][self.y - 1] == None:
                moves.append((self.x - 2, self.y - 1))
            elif board[self.x - 2][self.y - 1].get_color() != self.color:
                moves.append((self.x - 2, self.y - 1))
        #check if the knight can move up and right
        if self.x - 2 > -1 and self.y + 1 < 6:
            if board[self.x - 2][self.y + 1] == None:
                moves.append((self.x - 2, self.y + 1))
            elif board[self.x - 2][self.y + 1].get_color() != self.color:
                moves.append((self.x - 2, self.y + 1))
        #check if the knight can move down and left
        if self.x + 2 < 6 and self.y - 1 > -1:
            if board[self.x + 2][self.y - 1] == None:
                moves.append((self.x + 2, self.y - 1))
            elif board[self.x + 2][self.y - 1].get_color() != self.color:
                moves.append((self.x + 2, self.y - 1))
        #check if the knight can move down and right
        if self.x + 2 < 6 and self.y + 1 < 6:
            if board[self.x + 2][self.y + 1] == None:
                moves.append((self.x + 2, self.y + 1))
            elif board[self.x + 2][self.y + 1].get_color() != self.color:
                moves.append((self.x + 2, self.y + 1))
        #check if the knight can move left and up
        if self.x - 1 > -1 and self.y - 2 > -1:
            if board[self.x - 1][self.y - 2] == None:
                moves.append((self.x - 1, self.y - 2))
            elif board[self.x - 1][self.y - 2].get_color() != self.color:
                moves.append((self.x - 1, self.y - 2))
        #check if the knight can move left and down
        if self.x + 1 < 6 and self.y - 2 > -1:
            if board[self.x + 1][self.y - 2] == None:
                moves.append((self.x + 1, self.y - 2))
            elif board[self.x + 1][self.y - 2].get_color() != self.color:
                moves.append((self.x + 1, self.y - 2))
        #check if the knight can move right and up
        if self.x - 1 > -1 and self.y + 2 < 6:
            if board[self.x - 1][self.y + 2] == None:
                moves.append((self.x - 1, self.y + 2))
            elif board[self.x - 1][self.y + 2].get_color() != self.color:
                moves.append((self.x - 1, self.y + 2))
        #check if the knight can move right and down
        if self.x + 1 < 6 and self.y + 2 < 6:
            if board[self.x + 1][self.y + 2] == None:
                moves.append((self.x + 1, self.y + 2))
            elif board[self.x + 1][self.y + 2].get_color() != self.color:
                moves.append((self.x + 1, self.y + 2))
        return moves


class pawn(piece):
    def __init__(self):
        self.symbol="P"
        self.value=1
        self.name="pawn"
    def get_moves(self,board):
        moves = []
        #check if the pawn can move up
        if self.color==0:
            #white
            if self.y-1>-1:
                if board[self.x][self.y-1]==None:
                    moves.append((self.x,self.y-1))
                if self.x-1>-1:
                    if board[self.x-1][self.y-1]!=None and board[self.x-1][self.y-1].get_color()!=self.color:
                        moves.append((self.x-1,self.y-1))
                if self.x+1<5:
                    if board[self.x+1][self.y-1]==None and board[self.x+1][self.y-1].get_color()!=self.color:
                        moves.append((self.x+1,self.y-1))
        #check if the pawn can go down
        if self.color==1:
            #black
             if self.y+1<5:
                if board[self.x][self.y+1]==None:
                    moves.append((self.x,self.y+1))
                if self.x-1>-1:
                    if board[self.x-1][self.y+1]==None and board[self.x-1][self.y+1].get_color()!=self.colour:
                        moves.append((self.x-1,self.y+1))
                if self.x+1<5:
                    if board[self.x+1][self.y+1]==None and board[self.x+1][self.y+1].get_color()!=self.colour:
                        moves.append((self.x+1,self.y+1))

        return moves

        




        