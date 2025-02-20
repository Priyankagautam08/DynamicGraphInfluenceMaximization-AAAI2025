import pandas as pd
import numpy as np
import networkx as nx
from datetime import date, timedelta
import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd


class IMutil():
    def __init__(self):
        print("IM hep class is invoked")

    # # get IFC centrality score for each node
    # def get_inflcapapcity(self, g, uniinfweight):
    #     nodelist = list(g.nodes)
    #     il = np.zeros((len(nodelist), 1))
    #     ig = np.zeros((len(nodelist), 1))

    #     degn = max([nx.degree(g, ind) for ind in g.nodes])

    #     for countnode in range(len(nodelist)):
    #         tempw = 0
    #         for neighbnode in g.neighbors(nodelist[countnode]):
    #             tempw = tempw + uniinfweight * uniinfweight * nx.degree(g, neighbnode)

    #         # local score
    #         il[nodelist[countnode]] = 1 + list(g.degree([nodelist[countnode]], weight='weight'))[0][1] + tempw

    #         # global score
    #         ig[nodelist[countnode]] = nx.core_number(g)[nodelist[countnode]] * (
    #                     1 + (nx.degree(g, nodelist[countnode])) / (degn))

    #     # overall score
    #     ic = np.array([(il[nodelist[countnode]] / np.max(il)) * (ig[nodelist[countnode]] / np.max(ig)) for countnode in
    #                    range(len(nodelist))])

    #     return ic
    
    def calculate_ifc_score(G, uniinfweight=1.0):
        """
        Calculate the Influence Capacity (IFC) score for each node in the graph.

        Parameters:
            G (networkx.Graph): Input graph.
            uniinfweight (float): Weight factor for influence score calculation.

        Returns:
            dict: A dictionary mapping nodes to their IFC scores.
        """
        nodelist = list(G.nodes)
        il = np.zeros(len(nodelist))  # Local influence scores
        ig = np.zeros(len(nodelist))  # Global influence scores

        degn = max(dict(G.degree()).values())  # Maximum degree for normalization

        for idx, node in enumerate(nodelist):
            # Calculate local influence
            tempw = sum(uniinfweight * G.degree(neighb) for neighb in G.neighbors(node))
            il[idx] = 1 + G.degree(node) + tempw

            # Calculate global influence
            ig[idx] = nx.core_number(G)[node] * (1 + G.degree(node) / degn)

        # Normalize and calculate overall IFC score
        il_norm = il / np.max(il) if np.max(il) > 0 else il
        ig_norm = ig / np.max(ig) if np.max(ig) > 0 else ig
        ic_scores = il_norm * ig_norm

        return {node: ic_scores[idx] for idx, node in enumerate(nodelist)}

