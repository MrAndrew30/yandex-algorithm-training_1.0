N = int(input())
m = []
for _ in range(N):
    s = set(input() for _ in range(int(input())))
    m.append(s)

s1 = set()
s2 = m[0]
for s in m:
    s1 |= s
    s2 &= s
print(len(s2), *s2, sep="\n")
print(len(s1), *s1, sep="\n")
