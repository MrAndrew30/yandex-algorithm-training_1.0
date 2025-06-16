n = int(input())
d = {}
nums = map(int, input().split())

for i in range(n):
    d[i + 1] = next(nums)

k = int(input())
for index in map(int, input().split()):
    d[index] -= 1

for key in range(1, n+1):
    if d[key] >= 0:
        print("NO")
    else:
        print("YES")
