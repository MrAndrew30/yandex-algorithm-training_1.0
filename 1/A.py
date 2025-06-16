troom, tcond = map(int, input().split())
s = input()
if s == "heat":
    if tcond > troom:
        print(tcond)
    else:
        print(troom)
elif s == "freeze":
    if tcond < troom:
        print(tcond)
    else:
        print(troom)
elif s == "fan":
    print(troom)
else:
    print(tcond)
