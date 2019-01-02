import tools

n = 2

for m in range(9213, 9876):
    concatenation = ''

    for k in range(1, n + 1):
        concatenation += str(m * k)

    if tools.is_pandigital(concatenation):
        print(m, concatenation)

