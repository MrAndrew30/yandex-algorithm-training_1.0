m = map(int, input().split())
mx = [next(m), next(m)]
mn = [mx[0], mx[1]]
pr = mn[0] * mn[1]
for num in m:
    if any(i < num for i in mx):
        mx = [num, max(mx)]
    if any(i > num for i in mn):
        mn = [num, min(mn)]
if mx[0] * mx[1] > mn[0] * mn[1]:
    print(min(mx), max(mx))
else:
    print(min(mn), max(mn))
