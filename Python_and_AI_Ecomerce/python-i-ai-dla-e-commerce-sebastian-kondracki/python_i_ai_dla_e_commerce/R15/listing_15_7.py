import networkx as nx
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os
base_dir = os.path.dirname(__file__)

conn = sqlite3.connect(os.path.join(base_dir, "ue.sqlite3"))
df = pd.read_sql_query("SELECT user, product, event FROM user_event", conn)
G = nx.from_pandas_edgelist(df, "user", "product", ["event"])

pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos,
    node_color="red",
    edge_color="blue",
    alpha=0.9,
    labels={node: node for node in G.nodes()},
)
edge_labels = dict()
for n1, n2 in G.edges:
    edge_labels[(n1, n2)] = G[n1][n2]["event"]
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()