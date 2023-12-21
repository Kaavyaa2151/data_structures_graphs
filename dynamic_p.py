# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:18:56 2023

@author: kavya
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def printArr(self, dist):
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t {dist[i]}")

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Step 4: Print all distances
        self.printArr(dist)

# Create a new graph
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 4)
g.add_edge(2, 1, -3)
g.add_edge(2, 4, 6)
g.add_edge(3, 5, 3)
g.add_edge(4, 3, 1)
g.add_edge(4, 5, 2)

# Specify a different source vertex
src_vertex = 0


g.bellman_ford(src_vertex)

