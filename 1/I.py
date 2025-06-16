A, B, C, D, E = map(int, [input() for _ in range(5)])
x, y = min(A, B, C), sum((A, B, C)) - max((A, B, C)) - min((A, B, C))
D, E = max(D, E), min(D, E)

if x <= E and y <= D:
    print("YES")
else:
    print("NO")
