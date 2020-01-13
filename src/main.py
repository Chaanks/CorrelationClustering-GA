from utils import read_file_test
from individual import Individual

G = read_file_test('../data/data.txt')

i1 = Individual(G, method='random')
i2 = Individual(G, method='positive')

print(i1)
print(i2)