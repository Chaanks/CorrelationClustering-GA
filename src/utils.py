import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt

def read_file_test(file):
    G = nx.Graph()
    for x in open(file, "r"):
        if (len(x) > 1):
            x = x.split()
            start = int(x[0])
            end = int(x[1])
            weight = float(x[2])
            #G.add_edge(start, end, data={"affinity" :weight, "visited": False})
            G.add_edge(start, end, affinity=weight)
            #print(G[start][end]['affinity'])
    return G


def draw(G, partition, nb_cluster):
    colors = list(plt.cm.rainbow(np.linspace(0, 1, nb_cluster)))
    colors = [colors[i] for i in partition.tolist()]
    labels = nx.get_edge_attributes(G, 'affinity')
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color=colors,alpha=0.9, width=1, linewidths=2)
    #nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size= 12, font_color='red')
    plt.show()


def random_solution(G):
    nodes = np.asarray(G.nodes())
    partition = np.empty(nodes.shape, dtype=np.int32)
    nb_cluster = np.random.randint(1, nodes.shape[0])
    idx = 0
    
    while nodes.shape[0]:
        node = np.random.choice(nodes)
        partition[node] = idx 
        nodes = np.delete(nodes, np.where(nodes == node))
        if idx == nb_cluster-1:
            idx = 0
        else:
            idx += 1
    return partition, nb_cluster


def positive_solution(G):
    nodes = np.asarray(G.nodes())
    partition = np.empty(nodes.shape, dtype=np.int32)
    idx = 0
    
    while nodes.shape[0]:
        nodes = random_positive_path(G, nodes, partition, idx)
        idx +=1
    return partition, idx


def random_positive_path(G, nodes, part, idx):
    node = np.random.choice(nodes)
    nodes = np.delete(nodes, np.where(nodes == node))
    part[node] = idx
    while 1:
        neighbors = [edge[1] for edge in G.edges(node) if G[edge[0]][edge[1]]['affinity'] > 0 and edge[1] in nodes] 
        if len(neighbors) == 0:
            return nodes
        
        next_node = np.random.choice(neighbors)
        nodes = np.delete(nodes, np.where(nodes == next_node))
        node = next_node
        part[node] = idx