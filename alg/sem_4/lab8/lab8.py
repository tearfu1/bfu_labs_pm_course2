

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def minDistance(self, dist, sptSet):
        min = float("inf")
        min_index = -1
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def printSolution(self, dist):
        with open("output.txt", "w") as f:
            f.write("Vertex \tDistance from Source\n")
            for node in range(self.V):
                f.write(f"{node} \t{dist[node]}\n")

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

def read_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        vertices = int(lines[0])
        graph_matrix = [[int(val) for val in line.split()] for line in lines[1:]]
        return vertices, graph_matrix

def main():
    input_filename = "matrix.txt"
    vertices, graph_matrix = read_graph_from_file(input_filename)
    g = Graph(vertices)
    g.graph = graph_matrix
    source_vertex = 0  # Установите источниковую вершину
    g.dijkstra(source_vertex)

if __name__ == "__main__":
    main()
