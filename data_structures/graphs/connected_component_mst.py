import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
# G.add_edge(1, 5)
G.add_edge(2, 3)
# G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)
# G.add_edge(2, 6)

# explicitly set positions
pos = {
    1: (0, 1),
    2: (1, 0),
    3: (1, 2),
    4: (2, 2),
    5: (2, 0),
    6: (3, 1),
}

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

nx.draw_networkx(G, pos, **options, ax=ax1)

# Set margins for the axes so that nodes aren't clipped
ax1.margins(0.20)
ax1.axis("off")

nx.draw_networkx(G, pos, **options, ax=ax2)

# Draw a new edge (3, 4) in blue
nx.draw_networkx_edges(G, pos, edgelist=[(3, 4)], edge_color="red", width=5, ax=ax2)

# Set margins for the axes so that nodes aren't clipped
ax2.margins(0.20)
ax2.axis("off")

plt.show()