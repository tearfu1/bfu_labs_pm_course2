from dis_lab8 import *


def input_graph(path):
    with open(path, 'r') as f:
        n = int(f.readline())
        arcs = []
        for i in range(n):
            edge = list(map(int, f.readline().split()))
            edge[0] = edge[0] - 2
            edge[1] = edge[1] - 2
            arcs.append(edge)
    return n, arcs


def arcs_to_graph(arcs):
    n = len(arcs)
    v = 15
    graph = [[] for _ in range(v)]
    for i in range(n):
        graph[arcs[i][0]].append(arcs[i][1])
        graph[arcs[i][1]].append(arcs[i][0])
    return graph


def bellman_ford(graph_bf, color):
    # добавляем 2 новые вершины и сдвигаем все связи на 1
    graph_bf.insert(0, [])
    graph_bf.append([])
    # увеличиваем каждую вершину на 1, так как они сместились, после вставки вершины начала сети
    for i in range(len(graph_bf)):
        for j in range(len(graph_bf[i])):
            graph_bf[i][j] += 1
    # соединяем новые 2 вершины с разными долями
    for i in range(1, len(graph_bf) - 1):
        if color[i - 1] == 1:
            graph_bf[0].append(i)
            graph_bf[i].append(0)
        else:
            graph_bf[-1].append(i)
            graph_bf[i].append(len(graph_bf) - 1)
    # вывод нового графа( все вершины имеют номер n-1 относительно картинки)
    # for i in range(len(graph)):
    #     print(i, graph[i])
    # создание новой сети и вывод
    network = build_network(graph_bf, color)
    # for i in range(len(network)):
    #     print(network[i])
    max_flow(0, len(graph_bf) - 1, network)


# O(|v|^2 + |v||e|)
def khun(graph):
    # представление графа в виде матрицы смежности
    # adj_matrix = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    # for i in range(len(graph)):
    #     for j in graph[i]:
    #         adj_matrix[i][j] = 1

    def dfs(v):
        if used[v]:
            return False
        used[v] = True
        for to in graph[v]:
            if M[to] == -1 or dfs(M[to]):
                M[to] = v
                return True
        return False

    M = [-1 for _ in range(len(graph))]
    used = []
    for i in range(len(graph)):
        used = [False for i in range(len(graph))]
        dfs(i)

    print(f"Максимальный поток равен: {len(M)}, паросочетания: ", end="")
    for i in range(len(graph)):
        if M[i] != -1 and not used[M[i]]:
            used[i] = True
            print(i, " ", M[i], "; ", end="")


def main():
    path = "graph.txt"
    n, arcs = input_graph(path)
    arcs.sort()
    graph = arcs_to_graph(arcs)

    # проверка на двудольность
    color = [0 for _ in range(len(graph))]
    print(graph)
    for i in range(len(graph)):
        if color[i] == 0:
            def dfs(v, c):
                color[v] = c
                for u in graph[v]:
                    if (color[u] == 0):
                        dfs(u, (-1) * c)
                    elif (color[u] == c):
                        print(u, c)
                        return False
                return True

            if not dfs(i, 1):
                print("graph is not bipartite")
                break
    # вывод раскраски
    # for i in graph:
    #     for j in i:
    #         print(i, color[graph.index(i)], j, color[j])
    print("graph is bipartite")

    bellman_ford(graph, color)

    graph = arcs_to_graph(arcs)
    khun(graph)


main()
