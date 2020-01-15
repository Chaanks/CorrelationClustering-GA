import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from utils import read_file_test, draw
from population import Population


POPULATION_SIZE = 200
WHEEL_SIZE = 20
MUTATION_RATE = 0.1


class GA:

    def __init__(self, G):
        self.G = G
        self.population = Population(G, POPULATION_SIZE)
        self.generation = 0
        self.fittest = None


    def step(self):
        self.population.compute_fitness(self.G)
        self.fittest = self.population.get_fittest()
        #draw(self.G, self.fittest.genes, self.fittest.size)
        print('Iteration : ' + str(self.generation) + '\nFittest : \n' + str(self.fittest))
        self.crossover()
        self.mutation()
        self.generation += 1
    

    def selection(self):
        return self.population.wheel_selection(WHEEL_SIZE)
    

    def crossover(self):
        for i in range(self.population.population_size):
            p1 = self.selection()
            p2 = self.selection()

            # child is parent 1
            self.population.individuals[i].genes = np.copy(p1.genes)
            self.population.individuals[i].size = p1.size

            for j in range(len(self.population.individuals[i].genes)):
                r = np.random.randint(0, 2)
                gene = self.population.individuals[i].genes[j]
                genes_size = self.population.individuals[i].size
                # insert parent 2 gene in child
                if r == 1:
                    next_gene = p2.genes[j]
                
                    # case node cluster is not in child
                    if next_gene > genes_size:
                        # case we add a cluster -- pb lot of cluster with only 1 node
                        #self.population.individuals[i].genes[j] = genes_size
                        #self.population.individuals[i].size += 1
                        # case we add the node in a random cluster
                        r = np.random.randint(0, genes_size-1)
                        self.population.individuals[i].genes[j] = r
    

    def crossover_v2(self):
        for i in range(self.population.population_size):
            p1 = self.selection()
            p2 = self.selection()

            # child is parent 1
            self.population.individuals[i].genes = np.copy(p1.genes)
            self.population.individuals[i].size = p1.size

            for j in range(len(self.population.individuals[i].genes)):
                r = np.random.randint(0, 2)
                gene = self.population.individuals[i].genes[j]
                genes_size = self.population.individuals[i].size
                # insert parent 2 gene in child
                if r == 1:
                    next_gene = p2.genes[j]
                
                    # case node cluster is not in child
                    if next_gene > genes_size:
                        # case we add a cluster -- pb lot of cluster with only 1 node
                        #self.population.individuals[i].genes[j] = genes_size
                        #self.population.individuals[i].size += 1
                        # case we add the node in a random cluster
                        r = np.random.randint(0, genes_size-1)
                        self.population.individuals[i].genes[j] = r

    def mutation(self):
        
        # add cluster
        for i in range(self.population.population_size):
            r = np.random.uniform(0, 1)
            
            if MUTATION_RATE > r:

                r = np.random.uniform(0, 1)
                if r < 0.3:
                    self.population.individuals[i].add_cluster()
                else:
                    self.population.individuals[i].sub_cluster()