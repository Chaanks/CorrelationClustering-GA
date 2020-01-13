import matplotlib.pyplot as plt
import networkx as nx
import random

from utils import read_file_test


class GA:
    def __init__(self):
        self.G = read_file_test('../data/data.txt')
