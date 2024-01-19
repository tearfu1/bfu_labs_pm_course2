def rotate(a, b, c):
    return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])


def jarvis_march(a):
    n = len(a)
    p = [i for i in range(n)]
    for i in range(1, n):
        if a[p[i]][0] < a[p[0]][0]:
            p[i], p[0] = p[0], p[i]
    h = [p[0]]
    del p[0]
    p.append(h[0])
    while True:
        right = 0
        for i in range(1, len(p)):
            if rotate(a[h[-1]], a[p[right]], a[p[i]]) < 0:
                right = i
        if p[right] == h[0]:
            break
        else:
            h.append(p[right])
            del p[right]
    return h


a = [[1, 2], [3, 5], [6, 1], [8, 4], [10, 7], [7, 9], [4, 8], [2, 6], [9, 8], [4, 3], [5, 7]]
print(jarvis_march(a))
