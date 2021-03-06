import networkx as nx
import numpy as np
from random import randrange, random

from utils import random_solution, positive_solution


class Individual:

    def __init__(self, G, method='random'):
        self.genes = []
        self.size = 0
        self.fitness = 0
        self.method = None
        self.defects = []

        if method == 'random':
            self.genes, self.size = random_solution(G)
            self.method = 'random'
        elif method == 'positive':
            self.genes, self.size = positive_solution(G)
            self.method = 'positive'

    
    def compute_fitness(self, G):
        self.defects.clear()
        cost_in, cost_out = 0, 0
        data = nx.get_edge_attributes(G, 'affinity')
        for k, v in data.items():
            i, o = k[0], k[1]
            if self.genes[i] == self.genes[o] and v < 0:
                cost_in += abs(v)
                self.defects.append((i, o, 'inner'))
            elif self.genes[i] != self.genes[o] and v > 0:
                cost_out += v
                self.defects.append((i, o, 'outer'))

        self.fitness = cost_in + cost_out
        #print('cost in : ', cost_in)
        #print('cost out : ', cost_out)
        #print('total : ', cost)
        return self.fitness


    def get_fitness(self):
        return self.fitness

    
    def add_cluster(self):
        if self.size < len(self.genes):
            r = np.random.randint(0, len(self.genes))
            self.genes[r] = self.size
            self.size += 1
        self.remap()


    def sub_cluster(self):
        if self.size > 2:
            r = np.random.randint(0, self.size-1)
            for i in range(len(self.genes)):
                if self.genes[i] == r:
                    new_cluster = np.random.randint(0, self.size-1)
                    while new_cluster == r:
                        new_cluster = np.random.randint(0, self.size-1)
                    self.genes[i] = new_cluster
            self.size -= 1
            self.remap()


    def rand_cluster(self):
        if self.size > 1:
            r = [ np.random.randint(0, len(self.genes)-1) for i in range(2)]
            for i in r:
                self.genes[i] = np.random.randint(0, self.size-1)
            self.remap()


    def random_modification(self):
        r = np.random.randint(0, len(self.genes))
        self.genes[r] = np.random.randint(0, self.size-1)
        self.remap()

    def random_positive(self):
        if self.size > 1:
            n = np.random.randint(1, len(self.genes)//2)
            for _ in range(n):
                if len(self.defects) > 0:
                    idx = np.random.randint(0, len(self.defects))
                    edge = self.defects[idx]
                    del self.defects[idx]
                    node = edge[0] if random() < 0.5 else edge[1]

                    if edge[2] == 'inner':
                        self.genes[node] = np.random.randint(0, self.size-1)
                    else:
                        self.genes[node] = self.genes[edge[0]] if edge[0] != node else self.genes[edge[1]]
            self.remap()
        
    def remap(self):
        dic = {}
        cpt = 0
        for i in range(len(self.genes)):
            if  self.genes[i] not in dic:
                dic[self.genes[i]] = cpt
                cpt += 1

            self.genes[i] = dic[self.genes[i]]
        self.size = cpt


    def __gt__(self, idl):
        return self.fitness > idl.get_fitness()


    def __add__(self, idl): 
        return self.fitness + idl.get_fitness()


    def __str__(self):
        return '\tsize : ' + str(self.size) + '\n\tgenes : ' + str(self.genes) + ' \n\tfitness = ' + str(self.fitness) +  ' method -> ' + self.method + '\n'