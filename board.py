#Create a board class to represent the board
from pieces import *
import copy
#Create a board class to represent the board
class Board:
    def __init__(self):
        self.board = [[None for i in range(6)] for j in range(6)]
        self.board[0][0] = knight(1)
        self.board[1][0] = bishop(1)
        self.board[2][0] = rook(1)
        self.board[3][0] = king(1)
        self.board[4][0] = bishop(1)
        self.board[5][0] = knight(1)

        self.board[0][5] = knight(0)
        self.board[1][5] = bishop(0)
        self.board[2][5] = rook(0)
        self.board[3][5] = king(0)
        self.board[4][5] = bishop(0)
        self.board[5][5] = knight(0)
        for i in range(6):
            self.board[i][1] = pawn(1)
            self.board[i][4] = pawn(0)
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
    def printBoard(self):
        for j in range(6):
            for i in range(6):
                if self.board[i][j] == None:
                    print("  ", end = " ")
                else:
                    print(self.board[i][j].get_symbol(), end = " ")
            print()
    def getPiece(self, x, y):
        return self.board[x][y]
    def getBoard(self):
        return self.board
    def getPieceList(self, color):
        pieceList = []
        for i in range(6):
            for j in range(6):
                if self.board[i][j] != None:
                    if self.board[i][j].getColor() == color:
                        pieceList.append(self.board[i][j])
        return pieceList
    def getKing(self, color):
        for i in range(6):
            for j in range(6):
                if self.board[i][j] != None:
                    if self.board[i][j].getColor() == color and self.board[i][j].get_symbol() == "K":
                        return self.board[i][j]
    def draw(self):
        return self.stalemate(0) and self.stalemate(1)
    def getPieceList(self, color):
        pieceList = []
        for i in range(6):
            for j in range(6):
                if self.board[i][j] != None:
                    if self.board[i][j].get_color() == color:
                        pieceList.append(self.board[i][j])
        return pieceList
    
    def make_moves(self, piece,x,y,xn,yn):
        moveset=piece.get_moves(self.board,x,y)
        if (xn,yn) in moveset:
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
                    self.set_piece(xn,yn,temp)
                    return True
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
                    if self.board[row][col].get_color() == color and self.board[row][col].get_name() == "King":
                        return (row, col)
        return None
    def is_check(self, color):
        king = self.get_king(color)
        if king == None:
            return False
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() != color:
                        if king in self.board[row][col].get_moves(self.board, row, col):
                            return True
        return False
    def is_checkmate(self, color):
        if not self.is_check(color):
            return False
        for row in range(6):
            for col in range(6):
                if self.board[row][col] != None:
                    if self.board[row][col].get_color() == color:
                        for move in self.board[row][col].get_moves(self.board, row, col):
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
                        for move in self.board[row][col].get_moves(self.board, row, col):
                            new_board = copy.deepcopy(self)
                            new_board.set_piece(move[0], move[1], new_board.get_piece(row, col))
                            new_board.set_piece(row, col, None)
                            if not new_board.is_check(color):
                                return False
        return True
    def is_draw(self):
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

    

                           
    
    
