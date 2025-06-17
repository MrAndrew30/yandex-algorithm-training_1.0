import sys

bank = dict()

for s in sys.stdin:
    s = s.strip().split()
    if s[0] == "DEPOSIT":
        if s[1] not in bank:
            bank[s[1]] = 0
        bank[s[1]] += int(s[2])
    elif s[0] == "BALANCE":
        if s[1] in bank:
            print(bank[s[1]])
        else:
            print("ERROR")
    elif s[0] == "INCOME":
        p = int(s[1])
        for client in bank:
            if bank[client] > 0:
                income = int(bank[client] * (p / 100))
                bank[client] += income
    elif s[0] == "WITHDRAW":
        if s[1] not in bank:
            bank[s[1]] = 0
        bank[s[1]] -= int(s[2])
    elif s[0] == "TRANSFER":
        command, name1, name2, count = s
        count = int(count)
        if name1 not in bank:
            bank[name1] = 0
        if name2 not in bank:
            bank[name2] = 0
        bank[name1] -= count
        bank[name2] += count
