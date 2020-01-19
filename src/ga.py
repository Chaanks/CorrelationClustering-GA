from tqdm import tqdm
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import copy 

from utils import draw
from population import Population
from benchmark import Benchmark

POPULATION_SIZE = 128
WHEEL_SIZE = 8
MUTATION_RATE = 0.3


class GA:

    def __init__(self, G, filepath):
        self.benchmark = Benchmark(filepath)
        self.G = G
        self.population = Population(G, POPULATION_SIZE)
        self.generation = 0
        self.fittest = None


    def evolve(self):
        while 1:
            it = input('Iteration : ')
            for i in tqdm(range(int(it))):
                self.compute_fitness()
                if i % 10 == 0:
                    self.fittest = self.population.get_fittest()
                    self.benchmark.add(self.fittest.get_fitness())
                    self.benchmark.write('Iteration ' + str(self.generation) + ' Fittest ' + str(self.fittest.fitness))
                self.crossover()
                self.mutation()
                self.generation += 1
            stop = self.ask()
            if stop : break
    

    def compute_fitness(self):
        self.population.compute_fitness(self.G)


    def ask(self):
        print('Iteration : ' + str(self.generation) + '\nFittest : \n' + str(self.fittest))
        while 1:
            c = input('$ ')
            if c == 'graph':
                draw(self.G, self.fittest.genes, self.fittest.size)
            if c == 'show' or c == 'score':
                plt.figure()
                plt.plot([i for i in range(0, self.generation, 10)], self.benchmark.scores)
                plt.xlabel('iteration')
                plt.ylabel('score')
                plt.show()
            if c == 'top':
                top = np.partition(self.population.individuals, 5)[:5]
                for i in top:
                    print(i)
            if c == 'stop':
                return True
            if c == 'next' or c == '' or c == 'n':
                return False


    def selection(self):
        return self.population.wheel_selection(WHEEL_SIZE)
    

    def crossover(self):
        new_pop = Population(self.G, POPULATION_SIZE, empty=True)
        for i in range(self.population.population_size):
            p1 = self.selection()
            p2 = self.selection()
            while p1 == p2:
                p2 = self.selection()
            # map genes to get same cluster order
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
        for i in range(self.population.population_size):
            r = np.random.uniform(0, 1)
            
            if MUTATION_RATE > r:

                r = np.random.uniform(0, 1)
                if r < 0.5:
                    self.population.individuals[i].add_cluster()
                else:
                    self.population.individuals[i].sub_cluster()
            
                self.population.individuals[i].rand_cluster()