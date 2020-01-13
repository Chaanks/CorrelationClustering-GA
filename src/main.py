from utils import read_file_test, draw
from individual import Individual

G = read_file_test('../data/data.txt')

i1 = Individual(G, method='random')
i2 = Individual(G, method='positive')

print(i1)
print(i2)

draw(G, i1.genes, i1.size)
draw(G, i2.genes, i2.size)