def find_eulerian_cycle_recursive(graph, v, circuit):
    for u in range(len(graph[v])):
        if graph[v][u]:
            graph[v][u] = graph[u][v] = 0  # Remove edge
            find_eulerian_cycle_recursive(graph, u, circuit)
    circuit.append(v)

def find_eulerian_cycle(graph):
    circuit = []
    find_eulerian_cycle_recursive(graph, 0, circuit)
    return circuit[::-1]


def read_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        vertices = int(lines[0])
        graph_matrix = [[int(val) for val in line.split()] for line in lines[1:]]
        return vertices, graph_matrix


def write_cycle_to_file(cycle, file_path):
    with open(file_path, 'w') as file:
        file.write(' -> '.join(map(str, cycle)))


if __name__ == "__main__":
    input_file_path = "matrix.txt"
    output_file_path = "output.txt"

    # Read graph from input file
    v,g = read_graph_from_file(input_file_path)

    # Find Eulerian cycle
    eulerian_cycle = find_eulerian_cycle(g)

    # Write Eulerian cycle to output file
    write_cycle_to_file(eulerian_cycle, output_file_path)
