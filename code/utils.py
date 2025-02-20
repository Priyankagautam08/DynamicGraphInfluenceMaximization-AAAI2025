import networkx as nx
import pandas as pd
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt
# Import packages
#matplotlib inline

from random import uniform, seed
import numpy as np
import time
from igraph import *
import dgl
import torch
import torch.nn as nn
import torch.nn.functional as F
from dgl.data import DGLDataset
from dgl.dataloading import GraphDataLoader
import os
import torch
from torch.utils.data import TensorDataset, DataLoader

import dgl.nn as dglnn
import torch.nn as nn
import torch.nn.functional as F
#making a dataloader 
import torch
from torch.utils.data import Dataset, DataLoader
import networkx as nx
import dgl
import pickle
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
from torch.utils.data import DataLoader
torch.manual_seed(99)



def influence_spread(g, S, p=0.5, mc=10):
        """
        Input:  graph object, set of seed nodes, propagation probability
                and the number of Monte-Carlo simulations
        Output: spread: normalized average number of nodes influenced by the seed nodes
        """
        # Loop over the Monte-Carlo Simulations
        spread = []


        for i in range(mc):


            # Simulate propagation process
            new_active, A = S[:], S[:]


            while new_active:

                # For each newly active node, find its neighbors that become activated
                new_ones = []
                for node in new_active:
                    # Determine neighbors that become infected
                    np.random.seed(i)
                    outn = [n for n in g.neighbors(node)]
                    success = np.random.uniform(0, 1, len(outn)) < p
                    new_ones += list(np.extract(success, outn))


                new_active = list(set(new_ones) - set(A))


                # Add newly activated nodes to the set of activated nodes
                A += new_active


            spread.append(len(A))


        #return np.mean(spread) / len(g.nodes)
        return np.mean(spread)
    
def greedy(g, k, p=0.2, mc=1000):
    """
    Input:  graph object, number of seed nodes
    Output: optimal seed set, resulting spread, time for each iteration
    """

    S, spread, timelapse, start_time = [], [], [], time.time()

    # Find k nodes with largest marginal gain
    for _ in range(k):

        # Loop over nodes that are not yet in seed set to find biggest marginal gain
        best_spread = 0
        for j in set(range(len(g.nodes()))) - set(S):

            # Get the spread
            s = influence_spread(g, S + [j], p, mc)

            # Update the winning node and spread so far
            if s > best_spread:
                best_spread, node = s, j

        # Add the selected node to the seed set
        S.append(node)

        # Add estimated spread and elapsed time
        spread.append(best_spread)
        timelapse.append(time.time() - start_time)
        
    return S, spread, timelapse

def greedy_mod(g, k, candidatenodelist, p=0.5, mc=1000):

    """
    Input:  graph object, number of seed nodes
    Output: optimal seed set, resulting spread, time for each iteration
    """

    S, spread, timelapse, start_time = [], [], [], time.time()
    # S, spread, timelapse = [], [], []

    # Find k nodes with largest marginal gain
    for _ in range(k):

        # Loop over nodes that are not yet in seed set to find biggest marginal gain
        best_spread = 0

        # candidatenodelist = range(len(g.nodes))

        for j in set(candidatenodelist) - set(S):

            # Get the expected spread
            s = influence_spread(g, S + [j], p, mc)

            # Update the winning node and spread so far
            if s > best_spread:
                best_spread, node = s, j

        # Add the selected node to the seed set
        S.append(node)

        # Add estimated spread and elapsed time
        spread.append(best_spread)
        timelapse.append(time.time() - start_time)
        #print("k", _)

    return S, spread, timelapse

# get IFC centrality score for each node
def get_inflcapapcity(g, uniinfweight):
    nodelist = list(g.nodes)
    il = np.zeros((len(nodelist), 1))
    ig = np.zeros((len(nodelist), 1))

    degn = max([nx.degree(g, ind) for ind in g.nodes])

    for countnode in range(len(nodelist)):
        tempw = 0
        for neighbnode in g.neighbors(nodelist[countnode]):
            tempw = tempw + uniinfweight * uniinfweight * nx.degree(g, neighbnode)

        # local score
        il[nodelist[countnode]] = 1 + list(g.degree([nodelist[countnode]], weight='weight'))[0][1] + tempw

        # global score
        ig[nodelist[countnode]] = nx.core_number(g)[nodelist[countnode]] * (
                    1 + (nx.degree(g, nodelist[countnode])) / (degn))

    # overall score
    ic = np.array([(il[nodelist[countnode]] / np.max(il)) * (ig[nodelist[countnode]] / np.max(ig)) for countnode in
                    range(len(nodelist))])

    return ic

def graph_details(graph_dir):
    # Iterate over the gpickle files in the directory
    for file_name in os.listdir(graph_dir):
        if file_name.endswith('.gpickle'):
            # Construct the full file path
            file_path = os.path.join(graph_dir, file_name)
            
            # Load the graph from the gpickle file
            graph = nx.read_gpickle(file_path)
            
            # Get the number of nodes and edges
            num_nodes = graph.number_of_nodes()
            num_edges = graph.number_of_edges()
            
            # Print the number of nodes and edges
            print(f"Graph: {file_name}", "Number of nodes & edges :", num_nodes,  num_edges)
    return 1