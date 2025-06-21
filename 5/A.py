N = int(input())
m1 = [int(i) for i in input().split()]

M = int(input())
m2 = [int(i) for i in input().split()]
t1 = 0
t2 = 0

i1 = 0
i2 = 0
mn = abs(m1[0] - m2[0])

mn = abs(m1[0] - m2[0])
while t2 < M and t1 < N:
    if abs(m1[t1] - m2[t2]) == 0:
        i1 = t1
        i2 = t2
        break
    if abs(m1[t1] - m2[t2]) < mn:
        i1, i2 = t1, t2
        mn = abs(m1[t1] - m2[t2])
    if m1[t1] > m2[t2]:
        t2 += 1
    else:
        t1 += 1


print(m1[i1], m2[i2])
