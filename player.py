import pygame
from pieces import *
from board import *


#create a 500x500 window
pygame.init()
screen = pygame.display.set_mode((360, 360))
#set the window title
pygame.display.set_caption("6*6 Chess")
#set the background color
screen.fill((0, 0, 0))
#load images in
board = pygame.image.load("ISProj\\assets\\board.png")

#resize board image to 600*600
board1 = pygame.transform.scale(board, (360, 360))
screen.blit(board, (0, 0))

#create an exit loop
#create an instance of the board
board = Board()
running = True
update = True
while running:
    if update:
        #clear the display
        screen.fill((0, 0, 0))
        screen.blit(board1, (0, 0))
    for i in range(6):
        for j in range(6):
            if board.get_piece(i, j) != None:
                screen.blit(pygame.image.load("ISProj\\assets\\"+str(board.get_piece(i,j))+".png"), (i*60, j*60))
    #checking for mouse click
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(50*"-")
            board.printBoard()
            print(50*"-")
            if update:
                (x,y) = pygame.mouse.get_pos()
                x=x//60
                y=y//60
                if board.get_piece(x, y) != None:
                    choiceli=board.get_piece(x,y).get_moves(board.board,x,y)
                    print(x,y,board.get_piece(x,y).get_color())
                    print(choiceli)
                    for i in choiceli:
                        update=False
                        pygame.draw.rect(screen, (255, 0, 0), (i[0]*60, i[1]*60, 60, 60), 2)
            else:
                (xn,yn) = pygame.mouse.get_pos()
                xn=xn//60
                yn=yn//60
                if (xn,yn) in choiceli:
                    print(board.make_moves(board.get_piece(x,y),x=x,y=y,xn=xn,yn=yn))
                    update=True
                else:
                    update=True

    pygame.display.update()



