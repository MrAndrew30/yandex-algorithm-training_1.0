import sys

s = [i for i in sys.stdin]
t = set()
for i in range(len(s)):
    s[i] = s[i].replace("\n", " ")
    while "  " in s[i]:
        s[i] = s[i].replace("  ", " ")
    t |= set(s[i].split())
print(len(t))
