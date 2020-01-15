import numpy as np
import sys

from individual import Individual


class Population:

    def __init__(self, G, size, empty=False):
        self.population_size = size
        self.individuals = np.empty(size, dtype=np.object)

        if not empty:
            for i in range(len(self.individuals)):
                #if i%5 == 0:
                #    self.individuals[i] = Individual(G, method='random')
                #else:
                self.individuals[i] = Individual(G, method='positive')
    

    def compute_fitness(self, G):
        for i in self.individuals:
            i.compute_fitness(G)


    def get_fittest(self):
        fittest = None
        score = sys.maxsize
        for i in self.individuals:
            if i.get_fitness() < score:
                score = i.get_fitness()
                fittest = i
            if i.get_fitness() == score:
                r = np.random.uniform(0, 1)
                if r >= 0.5:
                    score = i.get_fitness()
                    fittest = i               
        return fittest


    def wheel_selection(self, size):
        pool = np.partition(self.individuals, size)[:size]
        m = sum([i.get_fitness() for i in pool])
        probs = [1/(i.get_fitness()/m) for i in pool]
        m = sum(probs)
        inv_probs = [i/m for i in probs]
        return pool[np.random.choice(len(pool), p=inv_probs)]

    def __str__(self):
        buff = ''
        for idx, i in enumerate(self.individuals):
            buff += 'Individual ' + str(idx) + '\n'
            buff += str(i)
        return buff