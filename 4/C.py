import sys

d = dict()
for text in sys.stdin:
    for word in text.split():
        if word not in d:
            d[word] = 0
        d[word] += 1
print(min(d.items(), key=lambda x: (-x[1], x[0]))[0])
