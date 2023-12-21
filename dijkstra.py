def dijkstra(graph, source):
    # Step 1: Initialize distances
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0

    # Step 2: Create a boolean array to track vertices included in the shortest path tree
    visited = {node: False for node in graph}

    # Step 3: Loop over all vertices
    for _ in range(len(graph)):
        # 3.1: Find the vertex with the minimum distance value from the set of vertices not yet included
        current_vertex = min_distance_vertex(distances, visited)
        visited[current_vertex] = True  # 3.2: Mark the vertex as included in the SPT

        # 3.3: Update the distance value of all adjacent vertices
        for neighbor, weight in graph[current_vertex].items():
            if not visited[neighbor] and distances[current_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + weight

    # Step 4: Print the solution
    print_solution(distances, source)

def min_distance_vertex(distances, visited):
    # Helper function to find the vertex with the minimum distance value
    min_distance = float('infinity')
    min_vertex = None

    for vertex, distance in distances.items():
        if distance < min_distance and not visited[vertex]:
            min_distance = distance
            min_vertex = vertex

    return min_vertex

def print_solution(distances, source):
    # Helper function to print the solution
    print("Vertex \t Distance from Source")
    for vertex, distance in distances.items():
        print(f"{vertex}\t {distance}")

# Example usage:
graph = {
    'A': {'B': 8, 'C': 4},
    'B': {'A': 1, 'C': 4, 'D': 5},
    'C': {'A': 5, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 3}
}
source_node = 'A'

dijkstra(graph, source_node)
