s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(*sorted(s1 & s2))
