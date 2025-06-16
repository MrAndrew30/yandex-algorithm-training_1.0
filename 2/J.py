n = int(input())
left = 30.0
right = 4000.0
prev = float(input())
for _ in range(n - 1):
    now, word = input().split()
    now = float(now)
    if word == "closer":
        if now > prev:
            left = max(left, (prev + now) / 2)
        else:
            right = min(right, (prev + now) / 2)
    else:
        if now > prev:
            right = min(right, (prev + now) / 2)
        else:
            left = max(left, (prev + now) / 2)
    prev = now

print(left, right)
