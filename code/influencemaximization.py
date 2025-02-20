import numpy as np
import time

class InfluenceMaximization:
    def __init__(self, graph, propagation_probability=0.5, monte_carlo=10):
        """
        Initialize the Influence Maximization class.
        
        Parameters:
            graph (networkx.Graph): The graph object.
            propagation_probability (float): Propagation probability.
            monte_carlo (int): Number of Monte Carlo simulations.
        """
        self.graph = graph
        self.p = propagation_probability
        self.mc = monte_carlo

    def influence_spread(self, S):
        """
        Calculate the influence spread using the Independent Cascade (IC) model.
        
        Parameters:
            S (list): Set of seed nodes.
        
        Returns:
            float: Average number of nodes influenced by the seed nodes.
        """
        spread = []  # Store the spread for each Monte Carlo simulation

        for i in range(self.mc):
            # Simulate the propagation process
            new_active, A = S[:], S[:]  # Initialize active nodes

            while new_active:
                new_ones = []
                for node in new_active:
                    # Randomly activate neighbors based on propagation probability
                    np.random.seed(i)
                    neighbors = list(self.graph.neighbors(node))
                    success = np.random.uniform(0, 1, len(neighbors)) < self.p
                    new_ones += list(np.extract(success, neighbors))
                
                # Deduplicate and find newly activated nodes
                new_active = list(set(new_ones) - set(A))
                A += new_active  # Add newly activated nodes to the influenced set

            spread.append(len(A))  # Store the total spread for this simulation

        return np.mean(spread)  # Average spread over all simulations

    def greedy(self, k):
        """
        Greedy algorithm for influence maximization.
        
        Parameters:
            k (int): Number of seed nodes to select.
        
        Returns:
            tuple: (optimal seed set, resulting spread, elapsed time per iteration)
        """
        S, spread, timelapse = [], [], []
        start_time = time.time()

        for _ in range(k):
            best_spread = 0
            for j in set(self.graph.nodes()) - set(S):
                # Calculate the spread if j is added to the seed set
                s = self.influence_spread(S + [j])
                if s > best_spread:
                    best_spread, node = s, j

            # Add the selected node to the seed set
            S.append(node)
            spread.append(best_spread)
            timelapse.append(time.time() - start_time)
        
        return S, spread, timelapse

    def greedy_mod(self, k, candidatenodelist):
        """
        Heuristic-based greedy algorithm for influence maximization.
        
        Parameters:
            k (int): Number of seed nodes to select.
            candidatenodelist (list): List of candidate nodes for seeding.
        
        Returns:
            tuple: (heuristic seed set, resulting spread, elapsed time per iteration)
        """
        S, spread, timelapse = [], [], []
        start_time = time.time()

        for _ in range(k):
            best_spread = 0
            for j in set(candidatenodelist) - set(S):
                # Calculate the spread if j is added to the seed set
                s = self.influence_spread(S + [j])
                if s > best_spread:
                    best_spread, node = s, j

            # Add the selected node to the seed set
            S.append(node)
            spread.append(best_spread)
            timelapse.append(time.time() - start_time)
        
        return S, spread, timelapse
