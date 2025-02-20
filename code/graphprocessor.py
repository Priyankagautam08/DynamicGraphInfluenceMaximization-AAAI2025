import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class GraphProcessor:
    def __init__(self, input_dir=None, output_dir=None, uniinfweight=1.0):
        """
        Initialize the GraphProcessor class.
        
        Parameters:
            input_dir (str): Directory containing input graphs (optional).
            output_dir (str): Directory to save processed graphs (optional).
        """
        self.uniinfweight = uniinfweight
        self.input_dir = input_dir
        self.output_dir = output_dir

    def calculate_ifc_score(self, G):
        nodelist = list(G.nodes)
        il = {}  # Local influence scores
        ig = {}  # Global influence scores

        degn = len(nodelist)

        for countnode, node in enumerate(nodelist):
            tempw = 0
            for neighbnode in G.neighbors(node):
                tempw += self.uniinfweight * self.uniinfweight * nx.degree(G, neighbnode)

            # Local score
            il[node] = 1 + list(G.degree([node], weight='weight'))[0][1] + tempw

            # Global score
            ig[node] = nx.core_number(G)[node] * (
                1 + (nx.degree(G, node)) / degn
            )

        # Combine local and global scores into a tuple
        ifc_scores = {node: (il[node], ig[node]) for node in nodelist}

        return ifc_scores


    def add_features_to_graph(self, G):
        # Calculate graph metrics
        degree = dict(G.degree())
        betweenness = nx.betweenness_centrality(G)
        k_core = nx.core_number(G)
        avg_neighbor_degree = nx.average_neighbor_degree(G)
        ifc_scores = self.calculate_ifc_score(G)

        # Add features to nodes
        for node in G.nodes:
            if node not in ifc_scores or len(ifc_scores[node]) < 1:
                print(f"Skipping node {node}: IFC scores missing or invalid")
                continue  # Skip this node if IFC scores are not valid

            # Add features
            G.nodes[node]["features"] = [
                degree[node],
                betweenness[node],
                k_core[node],
                avg_neighbor_degree[node],
                ifc_scores[node][0],  # Local influence score
            ]

        return G

    def add_labels_to_graph(self, G, top_percentage=40):
        """
        Add labels to ensure exactly `top_percentage` of nodes are labeled `1` based on IFC score.

        Parameters:
            G (networkx.Graph): The graph object.
            top_percentage (float): Percentage of nodes to label as `1` (default is 30%).

        Returns:
            networkx.Graph: The graph with labeled nodes.
        """
        # Extract IFC scores and sort nodes by IFC score in descending order
        nodes_with_scores = [(node, G.nodes[node]["features"][-1]) for node in G.nodes]
        sorted_nodes = sorted(nodes_with_scores, key=lambda x: x[1], reverse=True)

        # Determine the number of nodes to label as `1`
        num_top_nodes = int(len(sorted_nodes) * top_percentage / 100)

        # Label top `num_top_nodes` as `1` and the rest as `0`
        for i, (node, _) in enumerate(sorted_nodes):
            G.nodes[node]["label"] = 1 if i < num_top_nodes else 0

        return G

    def process_graphs(self):
        """
        Process all graphs in the input directory:
        - Add features
        - Add labels
        - Save the modified graphs
        """
        for file_name in os.listdir(self.input_dir):
            if file_name.endswith(".gpickle"):
                graph_path = os.path.join(self.input_dir, file_name)

                # Load the graph
                G = nx.read_gpickle(graph_path)

                # Add features and labels
                G = self.add_features_to_graph(G)
                G = self.add_labels_to_graph(G)

                # Save the modified graph
                output_path = os.path.join(self.output_dir, file_name)
                nx.write_gpickle(G, output_path)
                print(f"Processed and saved graph: {output_path}")
