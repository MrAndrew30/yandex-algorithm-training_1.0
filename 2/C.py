N = int(input())
m = map(int, input().split())
x = int(input())
ans = next(m)

for num in m:
    if abs(x - num) < abs(ans - x):
        ans = num

print(ans)
