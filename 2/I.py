def count_mines(i1, j1, m, N, M):
    ans = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if 0 <= i + i1 < N and 0 <= j + j1 < M and m[i + i1][j + j1] == "*":
                ans += 1
    return ans


N, M, K = map(int, input().split())
m = [[0] * M for _ in range(N)]
for _ in range(K):
    p, q = map(int, input().split())
    m[p - 1][q - 1] = "*"

for i in range(N):
    for j in range(M):
        if isinstance(m[i][j], int):
            m[i][j] = count_mines(i, j, m, N, M)

for i in range(N):
    print(*m[i])
