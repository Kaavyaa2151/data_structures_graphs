def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# Example usage:
visited = set()

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [6],
    5: [7],
    6: [],
    7: []
}

start_node = 1
dfs(visited, graph, start_node)
