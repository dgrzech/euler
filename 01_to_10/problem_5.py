divisors = [2, 3, 4, 5, 7, 9, 11, 13, 16, 17, 19]

n = 2 * 3 * 5 * 7 * 9 * 11 * 13 * 17 * 19
found = False

while not found:
    for d in divisors:
        if n % d != 0:
            n += 38
            break
        elif d == 19 and n % d == 0:
            found = True

print(n)
