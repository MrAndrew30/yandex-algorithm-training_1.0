N = int(input())
blocks = dict()
for _ in range(N):
    w, h = map(int, input().split())
    if w not in blocks:
        blocks[w] = h
    else:
        blocks[w] = max(blocks[w], h)
print(sum(blocks.values()))
