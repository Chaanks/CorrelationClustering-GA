import networkx as nx

from utils import random_solution, positive_solution


class Individual:

    def __init__(self, G, method='random'):
        self.genes = None
        self.size = 0
        self.fitness = 0

        if method == 'random':
            self.genes, self.size = random_solution(G)
        elif method == 'positive':
            self.genes, self.size = positive_solution(G)

    
    def compute_fitness(self, G):
        cost_in, cost_out = 0, 0
        data = nx.get_edge_attributes(G, 'affinity')
        for k, v in data.items():
            i, o = k[0], k[1]
            if self.genes[i] == self.genes[o] and v < 0:
                cost_in += abs(v)
            elif self.genes[i] != self.genes[o] and v > 0:
                cost_out += v

        self.fitness = cost_in + cost_out
        #print('cost in : ', cost_in)
        #print('cost out : ', cost_out)
        #print('total : ', cost)
        return self.fitness


    def get_fitness(self):
        return self.fitness


    def __str__(self):
        return '\tsize : ' + str(self.size) + '\n\tgenes : ' + str(self.genes) + ' \n\tfitness = ' + str(self.fitness) + '\n'