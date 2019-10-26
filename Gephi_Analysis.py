import networkx as nx
import matplotlib.pyplot as plt

# G = nx.gnp_random_graph(50, 0.3)

G = nx.barabasi_albert_graph(50, 2)

nx.draw(G)
plt.show()

nx.write_gexf(G, 'graph1.gexf')
