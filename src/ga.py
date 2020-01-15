import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import copy 

from utils import read_file_test, draw
from population import Population


POPULATION_SIZE = 128
WHEEL_SIZE = 8
MUTATION_RATE = 0.3


class GA:

    def __init__(self, G):
        self.G = G
        self.population = Population(G, POPULATION_SIZE)
        self.generation = 1
        self.fittest = None
        self.bench = []

    def step(self):
        self.compute_fitness()
        if self.generation % 100 == 0:
            self.show()
        if self.generation % 10 == 0:
            self.fittest = self.population.get_fittest()
            self.bench.append(self.fittest.get_fitness())
        self.crossover()
        self.mutation()
        self.generation += 1
    

    def compute_fitness(self):
        self.population.compute_fitness(self.G)


    def show(self):
        print('Iteration : ' + str(self.generation) + '\nFittest : \n' + str(self.fittest))
        c = input('show ? : ')
        if c == 'y' or c == 'yes':
            plt.figure()
            plt.plot([i for i in range(1, self.generation, 11)], self.bench)
            plt.xlabel('iteration')
            plt.ylabel('score')
            plt.show()
            draw(self.G, self.fittest.genes, self.fittest.size)
        if c == 'top':
            top = np.partition(self.population.individuals, 10)[:10]
            for i in top:
                print(i)


    def selection(self):
        return self.population.wheel_selection(WHEEL_SIZE)
    

    def crossover(self):
        new_pop = Population(self.G, POPULATION_SIZE, empty=True)
        for i in range(self.population.population_size):
            p1 = self.selection()
            p2 = self.selection()
            while p1 == p2:
                p2 = self.selection()
            # remap to get same cluster order
            p1.remap()
            p2.remap()

            # child is parent 1
            new_pop.individuals[i] = copy.deepcopy(p1)

            size = np.random.randint(0, len(p1.genes)//2)
            start = np.random.randint(0, len(p1.genes)-size)
            end = start + size

            for j in range(start, end):
                new_pop.individuals[i].genes[j] = p2.genes[j]
            
            new_pop.individuals[i].remap()

        self.population = new_pop

   
    def mutation(self):
        
        # add cluster
        for i in range(self.population.population_size):
            r = np.random.uniform(0, 1)
            
            if MUTATION_RATE > r:

                r = np.random.uniform(0, 1)
                if r < 0.5:
                    self.population.individuals[i].add_cluster()
                else:
                    self.population.individuals[i].sub_cluster()
            

                self.population.individuals[i].rand_cluster()
                #self.population.individuals[i].random_modification()