import neat
import numpy as np
import game
import random
import os
# create a function to evaluate the fitness of the neural network by playing a game between two genomes
def eval_genomes(genomes, config):
    #split genome array into two subarrays
    g1=genomes[:len(genomes)//2]
    g2=genomes[len(genomes)//2:]

    #create a list of genomes
    genome_list=[]
    #create a list of genomes that have been played
    played=[]
    #create a list of genomes that have not been played
    not_played=[]
    #start a game between each of genome 1 and 2 lists
    for i in range(len(g1)):

        #create a game
        g=game.game()      

        #create a neural network for each genome
        net1=neat.nn.FeedForwardNetwork.create(g1,config)
        net2=neat.nn.FeedForwardNetwork.create(g2,config)
        #add the neural network to the genome list
        genome_list.append((net1,g1))
        genome_list.append((net2,g2))
        
       
    #play the game until there are no more genomes to play



        