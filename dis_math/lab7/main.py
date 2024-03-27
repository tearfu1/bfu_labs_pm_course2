import numpy as np
from queue import Queue


def generate(n):
    G = []
    for i in range(n):
        deg = np.random.randint(10, 91)
        range1 = np.arange(i)
        range2 = np.arange(i + 1, n)
        all_range = np.union1d(range1, range2)
        G.append(np.random.choice(all_range, deg, replace=False).tolist())
    for i in range(3):
        for j in range(3, 7):
            if j not in G[i]:
                G[i].append(j)
                G[j].append(i)

    cnt = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            cnt += 1
    print("edges:", cnt)
    return G


def first(n, G):
    iters = 0
    u = 0
    q = Queue()
    q.put(u)
    dist = [float('inf')] * n
    dist[u] = 0
    while not q.empty():
        i = q.get()
        iters += 1
        for j in G[i]:
            iters += 1
            if dist[j] == float('inf'):
                dist[j] = dist[i] + 1
                q.put(j)
    print(dist)
    print(iters)


def second(n, G):
    iters = 0
    u = 0
    dist = [float('inf')] * n
    used = [False] * n
    dist[u] = 0
    for i in range(n):
        v = None
        for j in range(n):
            iters += 1
            if (not used[j]) and (v is None or dist[j] < dist[v]):
                v = j
        if dist[v] == float('inf'):
            break
        used[v] = True
        for e in G[v]:
            iters += 1
            if dist[v] + 1 < dist[e]:
                dist[e] = dist[v] + 1
    print(dist)
    print(iters)


def main():
    n = 1000
    G = generate(n)
    print('Vertices:', n)
    first(n, G)
    second(n, G)


main()
