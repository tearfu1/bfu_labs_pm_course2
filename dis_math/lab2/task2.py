def make_field(width, height):
    field = [[0] * (width + 1) for _ in range(height + 1)]
    for i in range(width + 1):
        field[0][i] = 1
    for j in range(height + 1):
        field[j][0] = 1
    return field


def count_paths(width, height):
    paths = make_field(width, height)

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

    return paths[height][width]


def count_paths_with_constraint(width, height):
    paths = make_field(width, height)

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if i > 1:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
            else:
                paths[i][j] = paths[i][j - 1]

    return paths[height][width]

width = 16
height = 13
result = count_paths(width, height)
result_with_constraint = count_paths_with_constraint(width, height)
print(result)
print(result_with_constraint)
