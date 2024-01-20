def matrix_to_graph(matrix):
    V = list(range(len(matrix)))
    E = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                E.append((i, j))

    return (V, E)


def bfs(G, source, destination):
    V, E = G
    d = [float('inf')] * len(V)
    d[source] = 0
    Q = [source]

    while Q:
        u = Q.pop(0)
        for edge in E:
            if edge[0] == u:
                v = edge[1]
                if d[v] == float('inf'):
                    d[v] = d[u] + 1
                    Q.append(v)

    return d[destination]


with open("matrix.txt") as f:
    matrix = f.readlines()
    matrix = [i.strip().split() for i in matrix]
    matrix = [list(map(int, i)) for i in matrix]

    graph = matrix_to_graph(matrix)
    print(bfs(graph, 0, 5))
