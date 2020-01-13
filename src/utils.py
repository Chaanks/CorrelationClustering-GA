import networkx as nx
import random 


def read_file_test(file):
    G = nx.Graph()
    for x in open(file, "r"):
        if (len(x) > 1):
            x = x.split()
            start = int(x[0])
            end = int(x[1])
            weight = x[2]
            #G.add_edge(start, end, data={"affinity" :weight, "visited": False})
            G.add_edge(start, end, affinity=weight)
            #print(G[start][end]['affinity'])
    return G


def random_solution(G):
    nodes = list(G.nodes())
    p = {}
    nb_cluster = random.randint(0, len(nodes)-1)
    idx = 0
    while nodes:
        node = random.choice(nodes)
        if not idx in p:
            p[idx] = []
        p[idx].append(node)
        nodes.remove(node)
        if idx == nb_cluster:
            idx = 0
        else:
            idx += 1
    return p


def positive_solution(G):
    nodes = list(G.nodes())
    p = {}
    idx = 0
    
    while nodes:
        node = random.choice(nodes)
        random_positive_path(G, nodes, p, idx)
        idx +=1
    return p


def random_positive_path(G, nodes, part, idx):
    node = random.choice(nodes)
    nodes.remove(node)
    part[idx] = [node]
    
    while 1:
        neighbors = [edge[1] for edge in G.edges(node) if G[edge[0]][edge[1]]['affinity'] == '+' and edge[1] in nodes]        
        if len(neighbors) == 0:
            return part
        
        next_node = random.choice(neighbors)
        nodes.remove(next_node)
        G[node][next_node]['visited'] = True   
        node = next_node
        part[idx].append(node)