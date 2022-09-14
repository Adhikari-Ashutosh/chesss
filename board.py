#Create a board class to represent the board
from pieces import *
import copy
#Create a board class to represent the board
import copy
#Create a board class to represent the board
class Board:
    def __init__(self):
        self.board = [[None for i in range(6)] for j in range(6)]
        self.board[0][0] = knight(1,0,0)
        self.board[1][0] = bishop(1,1,0)
        self.board[2][0] = rook(1,2,0)
        self.board[3][0] = king(1,3,0)
        self.board[4][0] = bishop(1,4,0)
        self.board[5][0] = knight(1,5,0)

        self.board[0][5] = knight(0,0,5)
        self.board[1][5] = bishop(0,1,5)
        self.board[2][5] = rook(0,2,5)
        self.board[3][5] = king(0,3,5)
        self.board[4][5] = bishop(0,4,5)
        self.board[5][5] = knight(0,5,5)
        for i in range(6):
            self.board[i][1] = pawn(1,i,1)
            self.board[i][4] = pawn(0,i,4)
        self.movehistory=[]
    def __str__(self):
        return str(self.board)
    def __repr__(self):
        return str(self.board)
    def __eq__(self, other):
        return self.board == other.board
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash((self.board))
    def get_board(self):
        return self.board
    def get_piece(self, row, col):
        return self.board[row][col]
    def set_piece(self, row, col, piece):
        self.board[row][col] = piece
        if piece!=None:
            piece.x=row
            piece.y=col
    def printBoard(self):
        for j in range(6):
            for i in range(6):
                if self.board[i][j] == None:
                    print("  ", end = " ")
                else:
                    print(self.board[i][j].get_symbol(), end = " ")
            print()
    def getPieceList(self, color):
        pieceList = []
        for i in range(6):
            for j in range(6):
                if self.board[i][j] != None:
                    if self.board[i][j].get_color() == color:
                        pieceList.append(self.board[i][j])
        return pieceList
    def getKing(self, color):
        for i in range(6):
            for j in range(6):
                if self.board[i][j] != None:
                    if self.board[i][j].get_color() == color and self.board[i][j].get_symbol() == "K":
                        return self.board[i][j]
    def draw(self):
        return self.stalemate(0) and self.stalemate(1)
    #define allowed moves during a check
    def allowed_moves(self,piece):
        allowed = []
        moveset=piece.get_moves(self)
        for move in moveset:
            newboard=copy.deepcopy(self)
            newboard.set_piece(piece.x,piece.y,None)
            newboard.set_piece(move[0],move[1],piece)
            
            if not newboard.is_check(piece.color):
                allowed.append((move[0],move[1]))
        return allowed
                                
    def make_moves(self, piece,x,y,xn,yn):
        moveset=piece.get_moves(self)
        allowed_moves=self.allowed_moves(piece)
        if (xn,yn) in moveset and (xn,yn) in allowed_moves:
            if self.board[xn][yn]!=None and self.board[xn][yn].get_color()!=piece.get_color():
                temp=self.get_piece(xn,yn)
                self.set_piece(xn,yn,self.get_piece(x,y))            
                self.set_piece(x,y,None)
                if self.is_check(piece.get_color()):
                    self.set_piece(x,y,self.get_piece(xn,yn))
                    self.set_piece(xn,yn,temp)
                    return False
                else:
                    self.set_piece(x,y,self.get_piece(xn,yn))
                    self.set_piece(x,y,None)
                    self.get_piece(xn,yn).x=xn
                    self.get_piece(xn,yn).y=yn
                    self.pawn_promotion(piece,piece.get_color(),xn,yn)
                    self.movehistory.append((x,y,xn,yn))
                    return True
            else:
                self.set_piece(xn,yn,self.get_piece(x,y))
                self.set_piece(x,y,None)
                self.get_piece(xn,yn).x=xn
                self.get_piece(xn,yn).y=yn
                self.pawn_promotion(piece,piece.get_color(),xn,yn)
                self.movehistory.append((x,y,xn,yn))
                return True
        else:
            return False
    def get_value(self, color):
        value = 0
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() == color:
                        value += self.board[row][col].get_value()
        return value
    def get_king(self, color):
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() == color and self.board[row][col].get_name() == "king":
                        return (row, col)
        return None
    def is_check(self, color):
        king = self.get_king(color)
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() != color:
                        if king in self.board[row][col].get_moves(self):
                            return True
        return False
    def is_checkmate(self, color):
        if not self.is_check(color):
            return False
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() == color:
                        for move in self.board[row][col].get_moves(self):
                            new_board = copy.deepcopy(self)
                            new_board.set_piece(move[0], move[1], new_board.get_piece(row, col))
                            new_board.set_piece(row, col, None)
                            if not new_board.is_check(color):
                                return False
        return True
    def is_stalemate(self, color):
        if self.is_check(color):
            return False
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() == color:
                        for move in self.board[row][col].get_moves(self):
                            new_board = copy.deepcopy(self)
                            new_board.set_piece(move[0], move[1], new_board.get_piece(row, col))
                            new_board.set_piece(row, col, None)
                            if not new_board.is_check(color):
                                return False
        return True
    def is_draw(self):
        #if last 6 alternate moves are same then draw
        if len(self.movehistory)>12:
            if self.movehistory[-1]==self.movehistory[-3] and self.movehistory[-2]==self.movehistory[-4] and self.movehistory[-5]==self.movehistory[-7] and self.movehistory[-6]==self.movehistory[-8]:
                return True
        if self.is_stalemate(0) or self.is_stalemate(1):
            return True
        return False
    def is_game_over(self):
        if self.is_checkmate(0) or self.is_checkmate(1) or self.is_draw():
            return True
        return False
    def get_winner(self):
        if self.is_checkmate(0):
            return 1
        elif self.is_checkmate(1):
            return 0
        else:
            return None
    def get_result(self):
        if self.is_checkmate(0):
            return "Black wins"
        elif self.is_checkmate(1):
            return "White wins"
        elif self.is_draw():
            return "Draw"
        else:
            return "Game not over"
    def pawn_promotion(self,piece,color, x, y):
        if piece.get_name()=="pawn":
            if color == 0:
                if y == 0:
                    self.set_piece(x, y, rook(color,x,y))
            else:
                if y == 5:
                    self.set_piece(x, y, rook(color,x,y))