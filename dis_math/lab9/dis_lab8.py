def get_max_vertex(k, V, S):
    m = 0  # наименьшее допустимое значение
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue

        if w[2] == 1:  # движение по стрелке
            if m < w[0]:
                m = w[0]
                v = i
        else:  # движение против стрелки
            if m < w[1]:
                m = w[1]
                v = i

    return v


def get_path(T):
    path = []
    for stamp in T:
        path.append(stamp[2])
    return path[2:3]


def get_max_flow(T):
    w = [x[0] for x in T]
    return min(*w)


def updateV(V, T, f):
    for t in T:
        if t[1] == -1:  # это исток
            continue

        sgn = V[t[2]][t[1]][2]  # направление движения

        # меняем веса в таблице для (i,j) и (j,i)
        V[t[1]][t[2]][0] -= f * sgn
        V[t[1]][t[2]][1] += f * sgn

        V[t[2]][t[1]][0] -= f * sgn
        V[t[2]][t[1]][1] += f * sgn


def build_network(graph, color):
    network = [[[0, 0, 1] for _ in range(len(graph))] for _ in range(len(graph))]

    for i in range(1, len(graph) - 1):
        for j in graph[i]:
            if j != 0 and j != len(graph) - 1:
                if color[i-1] == 1:
                    network[i][j] = [1, 0, 1]
                elif color[i-1] == -1:
                    network[i][j] = [1, 0, -1]
    for i in [0, len(graph) - 1]:
        for j in graph[i]:
            if i == 0:
                network[i][j] = [1, 0, 1]
                network[j][i] = [1, 0, -1]
            else:
                network[i][j] = [1, 0, -1]
                network[j][i] = [1, 0, 1]
    return network


def max_flow(start, finish, network):
    N = len(network)  # число вершин в графе
    init = start  # вершина истока (нумерация с нуля)
    end = finish  # вершина стока
    Tinit = (float('inf'), -1, init)  # первая метка маршруто (a, from, vertex)
    f = []  # максимальные потоки найденных маршрутов
    flows = []
    j = init
    while j != -1:
        k = init  # стартовая вершина (нумерация с нуля)
        T = [Tinit]  # метки маршрута
        S = {init}  # множество просмотренных вершин

        while k != end:  # пока не дошли до стока
            j = get_max_vertex(k, network, S)  # выбираем вершину с наибольшей пропускной способностью
            if j == -1:  # если следующих вершин нет
                if k == init:  # и мы на истоке, то
                    break  # завершаем поиск маршрутов
                else:  # иначе, переходим к предыдущей вершине
                    k = T.pop()[2]
                    continue

            c = network[k][j][0] if network[k][j][2] == 1 else network[k][j][1]  # определяем текущий поток
            T.append((c, j, k))  # добавляем метку маршрута
            S.add(j)  # запоминаем вершину как просмотренную

            if j == end:  # если дошди до стока
                f.append(get_max_flow(T))  # находим максимальную пропускную способность маршрута
                flows.append(get_path(T))
                updateV(network, T, f[-1])  # обновляем веса дуг
                break

            k = j
    F = sum(f)
    print(f"Максимальный поток равен: {F}, ребра из этих вершин: {flows}")
