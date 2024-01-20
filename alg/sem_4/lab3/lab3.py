MAXN = 1000  # Replace with the appropriate value for the maximum number of vertices

used = [False] * MAXN
comp = []

def bfs(g, v):
    queue = [v]
    used[v] = True
    comp.append(v)

    front = 0

    while front < len(queue):
        current = queue[front]
        front += 1

        for to in g[current]:
            if not used[to]:
                used[to] = True
                queue.append(to)
                comp.append(to)

def find_comps(number, g):
    n = number
    for i in range(n):
        used[i] = False

    for i in range(n):
        if not used[i]:
            comp.clear()
            bfs(g, i)

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
    find_comps(n,g)
