N = int(input())
s = set()
for _ in range(N):
    x, y = map(int, input().split())
    s.add(x)
print(len(s))
