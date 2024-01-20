MAXN = 1000  # Replace with the appropriate value for the maximum number of vertices

used = [False] * MAXN
comp = []


def dfs(v):
    used[v] = True
    comp.append(v)
    for to in g[v]:
        if not used[to]:
            dfs(to)


def find_comps(numbers, g):
    n = numbers
    for i in range(n):
        used[i] = False
    for i in range(n):
        if not used[i]:
            comp.clear()
            dfs(i)

            print("Component:", end="")
            for j in comp:
                print(f' {j}', end="")
            print()


with open("matrix.txt") as f:
    matrix = f.readlines()
    matrix = [i.strip().split() for i in matrix]
    matrix = [list(map(int, i)) for i in matrix]

    # matrix = [
    # [1, 0, 0, 0, 0, 0],
    # [0, 1, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0],
    # [0, 0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 1, 0],
    # [0, 0, 0, 0, 0, 1],]

    n = len(matrix)
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                g[i].append(j)
    find_comps(n, g)
