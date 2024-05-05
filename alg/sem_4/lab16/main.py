def findAns(k, s):
    if A[k][s] == 0:
        return
    if A[k - 1][s] == A[k][s]:
        findAns(k - 1, s)
    else:
        findAns(k - 1, s - w[k-1])
        ans.append(k)


N, W = map(int, input().split())
A = [[0 for _ in range(W+1)] for _ in range(N+1)]

p = list(map(int, input().split()))
w = list(map(int, input().split()))

for k in range(1, N+1):
    for s in range(1, W+1):
        if s >= w[k-1]:
            A[k][s] = max(A[k - 1][s], A[k - 1][s - w[k-1]] + p[k-1])
        else:
            A[k][s] = A[k - 1][s]
ans = []
findAns(N, W)
print(ans)