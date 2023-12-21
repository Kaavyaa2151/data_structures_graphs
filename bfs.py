# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:54:07 2023

@author: kavya
"""

from collections import defaultdict

def bfs(graph, start_node):
    # Step 1: Create a boolean dictionary 'visited' and initialize to False
    visited = defaultdict(bool)

    # Step 2: Create an empty queue
    queue = []

    # Step 3: Mark the current node as visited and enqueue it
    visited[start_node] = True
    queue.append(start_node)

    # Step 4: BFS traversal
    while queue:
        # Dequeue a vertex from the queue and print it
        current_node = queue.pop(0)
        print(current_node, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[current_node]:
            # If the neighbor has not been visited
            if not visited[neighbor]:
                # Mark it as visited
                visited[neighbor] = True
                # Enqueue the neighbor
                queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

start_node = 'A'
bfs(graph, start_node)
