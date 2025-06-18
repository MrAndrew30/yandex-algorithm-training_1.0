N, K = map(int, input().split())
cars = map(int, input().split())
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + next(cars)
ans = 0
t1, t2 = 0, 0
while t1 <= N and t2 <= N:
    s = prefix[t2] - prefix[t1]
    if s == K:
        ans += 1
        t2 += 1
    elif s > K:
        t1 += 1
    else:
        t2 += 1
print(ans)
