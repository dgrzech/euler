import math

p_max_no_solutions = 0
max_no_solutions = 0

for p in range(1001):
    solutions = []

    for c in range(3, p - 3):
        delta = c ** 2 + 2 * c * p - p ** 2
        if delta < 0:
            continue

        a1 = (p - c - math.sqrt(delta)) / 2
        b1 = p - c - a1

        a2 = (p - c + math.sqrt(delta)) / 2
        b2 = p - c - a2

        if (a1 > 0 and b1 > 0 and a1.is_integer() and b1.is_integer()) or (a2 > 0 and b2 > 0 and a2.is_integer() and b2.is_integer()):
            solutions.append([int(a1), int(b1), c])

    no_solutions = len(solutions)
    if p == 120:
        print(solutions)

    if no_solutions > max_no_solutions:
        p_max_no_solutions = p
        max_no_solutions = no_solutions

print(p_max_no_solutions, max_no_solutions)
