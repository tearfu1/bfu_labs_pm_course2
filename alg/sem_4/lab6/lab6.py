class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

def kruskal(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])#step 1 sort by weights

    mst = []
    disjoint_set = DisjointSet(n)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.union(u, v):
            mst.append((u, v, weight))

    return mst

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = [[int(val) for val in line.strip().split()] for line in lines]
    return graph

def write_mst_to_file(mst, filename):
    with open(filename, 'w') as file:
        file.write("Minimum Spanning Tree Edges:\n")
        for edge in mst:
            file.write(f"{edge[0]} - {edge[1]} : {edge[2]}\n")

if __name__ == "__main__":
    input_filename = "matrix.txt"
    output_filename = "output_mst.txt"

    graph = read_graph_from_file(input_filename)
    mst = kruskal(graph)
    print(mst)
    write_mst_to_file(mst, output_filename)

