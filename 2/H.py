m = map(int, input().split())
mx = [next(m), next(m), next(m)]
mn = [mx[0], mx[1], mx[2]]
pr = mn[0] * mn[1] * mn[2]
for num in m:
    if any(i < num for i in mx):
        mx = [num, max(mx), sum(mx) - max(mx) - min(mx)]
    if any(i > num for i in mn):
        mn = [num, min(mn), sum(mn) - max(mn) - min(mn)]
if mx[0] * mx[1] * mx[2] > min(mn) * (sum(mn) - max(mn) - min(mn)) * max(mx):
    print(mx[0], mx[1], mx[2])
else:
    print(min(mn), max(mx), sum(mn) - max(mn) - min(mn))
