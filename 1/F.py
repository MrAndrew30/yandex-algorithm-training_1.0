a1, a2, b1, b2 = map(int, input().split())
s1 = a1 + a2
s2 = b1 + b2
d = [((i + j) * max(s1 - i, s2 - j), (i + j, max(s1 - i, s2 - j)))
     for i in (a1, a2) for j in (b1, b2)]
d = sorted(d, key=lambda x: x[0])
print(*d[0][1])
