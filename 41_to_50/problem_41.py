import tools.py as tools

for n in range(7654321, 3, -2):
    if tools.is_pandigital(n) and str(n)[-1] != '5':
        if tools.is_prime(n):
            print('the largest n-digit pandigital number is ' + str(n))
            break
