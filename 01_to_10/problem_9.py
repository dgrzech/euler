for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - a - b
        if c ** 2 == a ** 2 + b ** 2:
            print(a, b, c, a * b * c)
