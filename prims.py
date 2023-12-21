INF = 9999999
V = 6
G = [[0, 4, 0, 0, 0, 0],
     [4, 0, 7, 8, 0, 0],
     [0, 7, 0, 5, 10, 0],
     [0, 8, 5, 0, 6, 12],
     [0, 0, 10, 6, 0, 14],
     [0, 0, 0, 12, 14, 0]]
selected = [0, 0, 0, 0, 0, 0]
no_edge = 0
selected[0] = True

print("Edge : Weight\n")

while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
