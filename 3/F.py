gen1 = input()
gen2 = input()
ans = 0
s2 = set(gen2[i-1] + gen2[i] for i in range(1, len(gen2)))
for i in range(1, len(gen1)):
    if gen1[i-1] + gen1[i] in s2:
        ans += 1
print(ans)
