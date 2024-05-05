def makeGraph(path):
    with open(path, 'r') as f:
        v, k = map(int, f.readline().split())
        edges = []
        for i in range(v):
            edges.append(list(map(int, f.readline().split())))
        return v, k, edges


def main():
    v, k, graph = makeGraph("input.txt")
    colors = set(range(1, k + 1))
    colored = [set()] * v
    colored[0] = {1}
    for i in range(1, v):
        usedColors = set()
        for neighbor in graph[i]:
            usedColors = usedColors.union(colored[neighbor])
        freeColors = colors.difference(usedColors)
        if len (freeColors) > 0:
            curColor = next(iter(freeColors))
            colored[i] = {curColor}
        else:
            return False
    return True


print(main())
