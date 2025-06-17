n = int(input())
synonyms = dict()
for _ in range(n):
    s1, s2 = input().split()
    synonyms[s1] = s2
    synonyms[s2] = s1
print(synonyms[input()])
