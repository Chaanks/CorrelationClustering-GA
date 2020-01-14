import numpy as np
import sys

from individual import Individual


class Population:

    def __init__(self, G, size):
        self.population_size = size
        self.individuals = np.empty(size, dtype=np.object)

        for i in range(len(self.individuals)):
            if i%2 == 0:
                self.individuals[i] = Individual(G, method='positive')
            else:
                self.individuals[i] = Individual(G, method='random')
    

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


    def wheel_selection(self):
        m = sum([i.get_fitness() for i in self.individuals])
        probs = [1/(i.get_fitness()/m) for i in self.individuals]
        m = sum(probs)
        inv_probs = [i/m for i in probs]
        #print(inv_probs, sum(inv_probs))
        return self.individuals[np.random.choice(len(self.individuals), p=inv_probs)]



    def __str__(self):
        buff = ''
        for idx, i in enumerate(self.individuals):
            buff += 'Individual ' + str(idx) + '\n'
            buff += str(i)
        return buff