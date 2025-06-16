import sys

text = " ".join(i.replace("\n", "") for i in sys.stdin)
d = dict()

for word in text.split():
    if word not in d:
        d[word] = 0
    d[word] += 1
items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(items[0][0])
