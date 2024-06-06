"""
=============
Edge Colormap
=============

Draw a graph with matplotlib, color edges.

Ref: https://networkx.org/documentation/stable/auto_examples/drawing/plot_edge_colormap.html#sphx-glr-auto-examples-drawing-plot-edge-colormap-py
"""

def edge_colormap():
    
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.star_graph(20)
    pos = nx.spring_layout(G, seed=63)  # Seed layout for reproducibility
    colors = range(20)
    options = {
        "node_color": "#A0CBE2",
        "edge_color": colors,
        "width": 4,
        "edge_cmap": plt.cm.Blues,
        "with_labels": False,
    }
    nx.draw(G, pos, **options)
    plt.show()
