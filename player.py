import pygame
from pieces import *
from board import *
import neat
from game import *
import os
def eval_genomes(genomes, config):
    #split genome array into two subarrays
    g1=genomes[:len(genomes)//2]
    g2=genomes[len(genomes)//2:]
    nets=[]
    #create a list of genomes
    genome_list=[]
    #start a game between each of genome 1 and 2 lists
    for i in range(len(g1)):
        g=game()
        #define nets
        g1[i][1].fitness=0
        g2[i][1].fitness=0

        net1=neat.nn.FeedForwardNetwork.create(g1[i][1],config)
        net2=neat.nn.FeedForwardNetwork.create(g2[i][1],config)
        nets.append(net1)
        nets.append(net2)
        #start game
        while g.CheckResult()==0:
            if g.turn==0:
                o=net1.activate(g.get_input())
                g1[i][1].fitness+=(g.score(0)*0.1-g.score(1)*0.1)
                #play move
                if not g.make_moves(int(o[0]),int(o[1]),int(o[2]),int(o[3])):
                    g1[i][1].fitness-=1
            else:
                o=net2.activate(g.get_input())
                g2[i][1].fitness+=(g.score(1)*0.1-g.score(0)*0.1)
                if not g.make_moves(int(o[0]),int(o[1]),int(o[2]),int(o[3])):
                    g2[i][1].fitness-=1
        if g.CheckResult()==1:
            g1[i][1].fitness+=10
            g2[i][1].fitness-=10
        if g.CheckResult()==-1:
            g1[i][1].fitness-=10
            g2[i][1].fitness+=10
        if g.CheckResult()==2:
            g1[i][1].fitness+=5
            g2[i][1].fitness+=5
        genome_list.append(g1[i])
        genome_list.append(g2[i])
def evaluation():
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-1174' )
    winner = p.run(eval_genomes, 1)
    return winner

#create a 500x500 window
pygame.init()
screen = pygame.display.set_mode((360, 360))
#set the window title
pygame.display.set_caption("6*6 Chess")
#set the background color
screen.fill((0, 0, 0))
#load images in
board = pygame.image.load("assets\\board.png")

#resize board image to 600*600
board1 = pygame.transform.scale(board, (360, 360))
screen.blit(board1, (0, 0))

#create an exit loop
#create an instance of the board
g = game()
running = True
update = True
model=evaluation()
config_file=os.path.join('config-feedforward.txt')
config=neat.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_file)
net=neat.nn.FeedForwardNetwork.create(model,config)
while running:
    if update:
        #clear the display
        screen.fill((0, 0, 0))
        screen.blit(board1, (0, 0))
    for i in range(6):
        for j in range(6):
            if g.board.get_piece(i, j) != None:
                screen.blit(pygame.image.load("assets\\"+str(g.board.get_piece(i,j))+".png"), (i*60, j*60))
    #checking for mouse click
    if g.board.is_check(g.turn):
        pygame.draw.rect(screen, (0, 0, 255), (g.board.get_king(g.turn)[0]*60, g.board.get_king(g.turn)[1]*60, 60, 60), 2)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(50*"-")
            g.board.printBoard()
            print(50*"-")
            
            if update:
                if g.turn==0:
                    (x,y) = pygame.mouse.get_pos()
                    x=x//60
                    y=y//60
                    if g.board.get_piece(x, y) != None and g.board.get_piece(x, y).get_color() == g.turn:
                        choiceli=g.board.get_piece(x,y).get_moves(g.board)
                        print(x,y,g.board.get_piece(x,y).get_color())
                        print(choiceli)
                        if g.board.is_check(g.turn):
                            choiceli=g.board.allowed_moves(g.board.get_piece(x,y))
                            print(choiceli)
                        for i in choiceli:
                            update=False
                            pygame.draw.rect(screen, (255, 0, 0), (i[0]*60, i[1]*60, 60, 60), 2)
                        
                else:
                    o=net.activate(g.get_input())
                    g.make_moves(int(o[0]),int(o[1]),int(o[2]),int(o[3]))
                    update=True
            else:
                (xn,yn) = pygame.mouse.get_pos()
                xn=xn//60
                yn=yn//60
                if (xn,yn) in choiceli:
                    print(g.board.make_moves(g.board.get_piece(x,y),x=x,y=y,xn=xn,yn=yn))
                    g.turn=1-g.turn
                    update=True
                else:
                    update=True
        

    pygame.display.update()



