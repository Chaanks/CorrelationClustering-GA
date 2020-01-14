from utils import read_file_test, draw

from individual import Individual
from population import Population
from ga import GA


def test_individual():
    G = read_file_test('../data/data.txt')

    i1 = Individual(G, method='random')
    #i2 = Individual(G, method='positive')

    i1.compute_fitness(G)
    #i2.compute_fitness(G)

    print(i1)
    #print(i2)

    i1.add_cluster()

    #draw(G, i1.genes, i1.size)
    #draw(G, i2.genes, i2.size)


def test_population():
    p1 = Population(G, 3)
    p1.compute_fitness(G)
    print(p1)
    print(p1.get_fittest())
    print(p1.wheel_selection())



def test_genetic_algorithm():
    G = read_file_test('../data/data_30_218.txt')
    ga = GA(G)
    for i in range(1000):
        ga.step()
    
    while 1:
        i = input()
        if i == 's':
            break


def test_mutation():
    G = read_file_test('../data/data.txt')
    ga = GA(G)
    ga.mutation()


#test_individual()
test_genetic_algorithm()
#test_mutation()