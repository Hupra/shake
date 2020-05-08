import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

def draw_graph(g):

    G = nx.DiGraph()
    G.add_nodes_from(g.vers())
    G.add_weighted_edges_from(g.edges())

    fig, ax = plt.subplots(1, 1, figsize=(20, 20))
    options = {
        'arrows': True,
        'arrowstyle': '-|>',
        'arrowsize': 12,
        'node_size': 3000,
        "ax": ax
    }

    pos = nx.spring_layout(G, k=4, iterations=100)

    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx(G, pos, **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()

def draw_graph_mst(g, s):

    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    ax[0].set_facecolor("#232323")
    ax[1].set_facecolor("#232323")
    options = {
        'arrows': True,
        'arrowstyle': '-|>',
        'arrowsize': 12,
        'node_size': 3000,
        #'font_family': 'Times New Roman',
        'font_size': 30
    }
    edge_option = {
        'font_size': 18,
        'font_color': "white",
        'bbox': dict(color="#232323")
    }

    G = nx.DiGraph()
    G.add_nodes_from(g.vers())
    G.add_weighted_edges_from(g.edges())
    pos = nx.spring_layout(G, k=4, iterations=100, seed=33)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos, **options, ax=ax[0], edge_color="grey")
    #nx.draw_networkx(G, pos, **options, ax=ax[1], edge_color="grey")
    nx.draw_networkx_nodes(G, pos, **options, ax=ax[0], node_color='#ADD8E6', nodelist=[s])
    nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax[0], **edge_option)

    g = g.mst(s)
    G2 = nx.DiGraph()
    G2.add_nodes_from(g.vers())
    G2.add_weighted_edges_from(g.edges())
    edge_labels = nx.get_edge_attributes(G2, 'weight')

    nx.draw_networkx(G2, pos, **options, ax=ax[1], edge_color="green")
    nx.draw_networkx_nodes(G2, pos, **options, ax=ax[1], node_color='#ADD8E6', nodelist=[s])
    nx.draw_networkx_edge_labels(G2, pos, edge_labels, ax=ax[1], **edge_option)

    plt.show()
