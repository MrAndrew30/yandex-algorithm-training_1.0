a = int(input())
b = int(input())
c = int(input())

if c >= 0:
    if a == 0 and c * c == b:
        print("MANY SOLUTIONS")
    elif a == 0 and c * c != b or \
            (c * c - b) % a != 0:
        print("NO SOLUTION")
    else:
        print((c * c - b) // a)
else:
    print("NO SOLUTION")
