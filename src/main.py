import sys
from utils import read_file
from ga import GA


filepath = sys.argv[1]
print('graph : ', filepath)
G = read_file('../data/' + filepath)
ga = GA(G, filepath)
ga.evolve()