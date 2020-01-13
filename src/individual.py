from utils import random_solution, positive_solution

class Individual:

    def __init__(self, G, method='random'):
        self.genes = {}
        self.fitness = 0

        if method == 'random':
            self.genes = random_solution(G)
        elif method == 'positive':
            self.genes = positive_solution(G)
    
    def __str__(self):
        return 'genes : ' + str(self.genes) + ' \nfitness = ' + str(self.fitness) + '\n'