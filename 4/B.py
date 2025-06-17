with open("input.txt") as file:
    d = {}
    for row in file:
        row = row.strip().split()
        for word in row:
            if word not in d:
                d[word] = 0
            print(d[word], end=" ")
            d[word] += 1
