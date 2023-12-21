def FloydWarshall(n, A):
    # A is the adjacency matrix representing the graph
    # Initialize the matrix for k = 0 (direct connections)
    Ak = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            Ak[0][i][j] = A[i][j]

    # Iterate for each intermediate vertex k
    for k in range(n):
        # Iterate over all pairs of vertices i, j
        for i in range(n):
            for j in range(n):
                # Update the shortest path if the path through vertex k is shorter
                Ak[k][i][j] = min(Ak[k-1][i][j], Ak[k-1][i][k] + Ak[k-1][k][j])

    # Return the final matrix representing the shortest paths between all pairs of vertices
    return Ak[n - 1]

# Example usage:
n = 5
A = [
    [0, 3, float('inf'), 7, float('inf')],
    [8, 0, 2, float('inf'), float('inf')],
    [5, float('inf'), 0, 1, 4],
    [2, float('inf'), float('inf'), 0, 6],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

result = FloydWarshall(n, A)

# Print the final matrix
for row in result:
    print(row)
