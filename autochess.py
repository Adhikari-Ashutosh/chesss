import sys
import neat
import numpy as np
import game
import random
import os
import pickle
# create a function to evaluate the fitness of the neural network by playing a game between two genomes

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
        moves=200
        net1=neat.nn.FeedForwardNetwork.create(g1[i][1],config)
        net2=neat.nn.FeedForwardNetwork.create(g2[i][1],config)
        nets.append(net1)
        nets.append(net2)
        #start game
        while g.CheckResult()==0 and moves>0:
            if g.turn==0:
                o=net1.activate(g.get_input())
                g1[i][1].fitness+=(g.score(0)*0.01-g.score(1)*0.01)
                #play move
                if not g.make_moves(int(o[0]),int(o[1]),int(o[2]),int(o[3])):
                    g1[i][1].fitness-=5
            else:
                o=net2.activate(g.get_input())
                g2[i][1].fitness+=(g.score(1)*0.01-g.score(0)*0.01)
                if not g.make_moves(int(o[0]),int(o[1]),int(o[2]),int(o[3])):
                    g2[i][1].fitness-=5
            moves-=1
        if moves<0:
            g1[i][1].fitness-=10
            g2[i][1].fitness-=10
        if g.CheckResult()==1:
            g1[i][1].fitness+=5
            g2[i][1].fitness-=5
        if g.CheckResult()==-1:
            g1[i][1].fitness-=5
            g2[i][1].fitness+=5
        if g.CheckResult()==2:
            g1[i][1].fitness-=1
            g2[i][1].fitness-=1
        
        genome_list.append(g1[i])
        genome_list.append(g2[i])
#define run function
def run(config_file):
    #load config file
    config=neat.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_file)
    #create population
#     p=neat.Population(config)
    p=neat.Checkpointer.restore_checkpoint('./neat-checkpoint-1224')
    
    #create a reporter
    p.add_reporter(neat.StdOutReporter(True))
    stats=neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(25))
    #run for 100 generations
    winner=p.run(eval_genomes,3600)
    #save winner
    with open('winner.pkl','wb') as output:
        pickle.dump(winner,output,1)
    #show stats
    print(stats)
    print(winner)
#start running
if __name__=='__main__':
    config_path=os.path.join('../input/datatat/config-feedforward.txt')
    run(config_path)