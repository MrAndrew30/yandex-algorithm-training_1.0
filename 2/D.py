m = map(int, input().split())

ans = 0
try:
    prev = next(m)
    now = next(m)
    for num in m:
        nxt = num
        if now > nxt and now > prev:
            ans += 1
        prev, now = now, nxt
except:
    ...

print(ans)
