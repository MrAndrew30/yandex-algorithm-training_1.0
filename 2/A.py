s = map(int, input().split())
flag = True
prev = next(s)
for num in s:
    if num <= prev:
        flag = False
    prev = num

if flag:
    print("YES")
else:
    print("NO")
