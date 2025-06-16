x, y, z = map(int, input().split())
s1 = set(int(i) for i in input())
s2 = set((x, y, z))
print(len(s1.difference(s2)))
