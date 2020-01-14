from utils import read_file_test, draw
from individual import Individual
from population import Population


G = read_file_test('../data/data.txt')


def test_individual():
    i1 = Individual(G, method='random')
    i2 = Individual(G, method='positive')

    i1.compute_fitness(G)
    i2.compute_fitness(G)

    print(i1)
    print(i2)

    #draw(G, i1.genes, i1.size)
    #draw(G, i2.genes, i2.size)


def test_population():
    p1 = Population(G, 3)
    p1.compute_fitness(G)
    print(p1)
    print(p1.get_fittest())
    print(p1.wheel_selection())


test_population()