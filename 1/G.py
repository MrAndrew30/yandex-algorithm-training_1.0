N, K, M = map(int, input().split())

x = N
ans = 0
while x >= K and M <= K:
    t = (x // K) * (K // M)
    ans += t
    x -= t * M

print(ans)
