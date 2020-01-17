from utils import read_file, draw

from individual import Individual
from population import Population
from ga import GA


def test_individual():
    G = read_file('../data/data.txt')

    i1 = Individual(G, method='random')
    i2 = Individual(G, method='positive')

    i1.compute_fitness(G)
    #i2.compute_fitness(G)

    print(i1)
    print(i2)

    i1.remap()
    i2.remap()

    print(i1)
    print(i2)
    #i1.add_cluster()

    #draw(G, i1.genes, i1.size)
    #draw(G, i2.genes, i2.size)


def test_population():
    G = read_file('../data/data.txt')
    p1 = Population(G, 3)
    p1.compute_fitness(G)
    print(p1)
    print(p1.get_fittest())
    print(p1.wheel_selection(10))

def test_mutation():
    G = read_file('../data/data.txt')
    ga = GA(G)
    ga.mutation()


def test_crossover():
    G = read_file('../data/data.txt')
    ga = GA(G)
    ga.compute_fitness()

#test_individual()
#test_mutation()
#test_crossover()