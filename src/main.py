from utils import read_file
from ga import GA

G = read_file('../data/file_200_0.1.g')
ga = GA(G)
ga.evolve()