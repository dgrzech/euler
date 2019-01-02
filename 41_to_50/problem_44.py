import math


def pentagonal_number(n):
    return int(n * (3 * n - 1) / 2)


pentagonal_numbers_list = []
i = 1
found = False

while not found:
    pentagonal_number_i = pentagonal_number(i)
    pentagonal_numbers_list.append(pentagonal_number_i)
    i += 1

    for number in reversed(pentagonal_numbers_list[:-1]):
        s = pentagonal_number_i + number
        n_sum = (1 + math.sqrt(24 * s + 1)) / 6

        if not n_sum.is_integer():
            continue

        diff = pentagonal_number_i - number
        n_diff = (1 + math.sqrt(24 * diff + 1)) / 6

        if n_diff.is_integer():
            print(pentagonal_number_i, number, diff)
            found = True
