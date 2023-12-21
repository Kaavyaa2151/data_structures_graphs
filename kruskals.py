def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    root_u, root_v = find(u), find(v)
    parent[root_u] = root_v

# Different set of example edges
edges = [
    (4, 0, 1),
    (2, 0, 2),
    (5, 1, 2),
    (1, 1, 3),
    (3, 2, 3),
    (6, 2, 4),
    (7, 3, 4)
]

# Sort edges based on weights
edges.sort()

# Initialize parent array
# For simplicity, assume each node is its own parent initially
n = max(max(u, v) for _, u, v in edges) + 1
parent = list(range(n))

mst = []

# Iterate through sorted edges
for weight, u, v in edges:
    # Check for cycles
    if find(u) != find(v):
        # Union and add edge to mst
        union(u, v)
        mst.append((weight, u, v))

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"Edge: {edge[1]} - {edge[2]}, Weight: {edge[0]}")
