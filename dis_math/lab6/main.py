def input_graph(path):
    graph = []
    with open(path) as f:
        n = int(f.readline())
        for i in range(n):
            graph.append(list(map(int, f.readline().split())))
    return graph


def create_adj_matrix(v, graph):
    adj_matrix = [[0 for _ in range(v)] for _ in range(v)]
    for i in range(len(graph)):
        adj_matrix[graph[i][0]][graph[i][1]] = 1
    return adj_matrix


def adj_to_inc_matrix(adj_matrix):
    inc_matrix = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            is_arc = False
            arc = [0 for _ in range(len(adj_matrix))]
            if adj_matrix[i][j] == 1:
                arc[i] = 1
                arc[j] = -1
                is_arc = True
            if is_arc:
                inc_matrix.append(arc)
    return inc_matrix


def vertex_degrees(graph):
    vertex_degrees = {}
    for i in range(len(graph)):
        vertex = graph[i][0]
        if vertex in vertex_degrees:
            vertex_degrees[vertex] += 1
        else:
            vertex_degrees[vertex] = 1
    return vertex_degrees


def output_matrix(matrix, atr=""):
    print(atr)
    for i in range(len(matrix)):
        print(matrix[i])
    print()


def bellmanFord(n, graph):
    s = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                s[i][j] = float('inf')
    for t in range(len(graph)):
        i = graph[t][0]
        j = graph[t][1]
        s[i][j] = graph[t][2]
        s[j][i] = graph[t][2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s[i][j] = min(s[i][j],
                              s[i][k] + s[k][j])
    output_matrix(s)


def main():
    # input graph
    path = "input.txt"
    graph = input_graph(path)
    # create adj_matrix
    adj_matrix = create_adj_matrix(8, graph)
    output_matrix(adj_matrix, "adjacency matrix")
    inc_matrix = adj_to_inc_matrix(adj_matrix)
    output_matrix(inc_matrix, "adjacency matrix")
    # vertex degrees > 2 => в графе нет Эйлерова пути => граф не Эйлеров
    print(vertex_degrees(graph))
    # кратчайшие пути
    bellmanFord(8, graph)


if __name__ == '__main__':
    main()
