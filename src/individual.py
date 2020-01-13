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
    
    def __str__(self):
        return 'size : ' + str(self.size) + ' genes : ' + str(self.genes) + ' \nfitness = ' + str(self.fitness) + '\n'