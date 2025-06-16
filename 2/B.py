values = ("CONSTANT", "ASCENDING",
          "DESCENDING", "WEAKLY ASCENDING",
          "WEAKLY DESCENDING", "RANDOM")

d = {i: True for i in values}

prev = int(input())
x = int(input())
while x != -2 * 10 ** 9:
    if prev != x:
        d["CONSTANT"] = False
    else:
        d["ASCENDING"] = False
        d["DESCENDING"] = False
    if x > prev:
        d["DESCENDING"] = False
        d["WEAKLY DESCENDING"] = False
    elif x < prev:
        d["ASCENDING"] = False
        d["WEAKLY ASCENDING"] = False
    prev = x
    x = int(input())

flag = True
for i in values:
    if d[i] and flag:
        print(i)
        flag = False
