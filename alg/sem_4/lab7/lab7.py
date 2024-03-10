def prim(adj_matrix):
  n = len(adj_matrix)
  visited = [False] * n
  mst = []

  # Выбор начальной вершины
  visited[0] = True
  for i in range(n):
    if adj_matrix[0][i] != -1:
      mst.append((0, i, adj_matrix[0][i]))
      break

  # Добавление остальных вершин
  for _ in range(n - 1):
    min_weight = float('inf')
    u = -1
    v = -1

    # Поиск ребра с минимальным весом, соединяющим
    # посещенную и непосещенную вершины
    for i in range(n):
      if visited[i]:
        for j in range(n):
          if not visited[j] and adj_matrix[i][j] != -1 and adj_matrix[i][j] != 0:
            if adj_matrix[i][j] < min_weight:
              min_weight = adj_matrix[i][j]
              u = i
              v = j

    # Добавление ребра в MST
    mst.append((u, v, min_weight))
    visited[v] = True

  return mst


def main():
  # Чтение данных из файла
  with open("matrix.txt", "r") as f:
    n = int(f.readline())
    adj_matrix = [list(map(int, line.split())) for line in f]

  # Поиск минимального остовного дерева
  mst = prim(adj_matrix)

  # Запись результата в файл
  with open("output.txt", "w") as f:
    for edge in mst:
      f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")


if __name__ == "__main__":
  main()
