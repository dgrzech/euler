import math

s = 0
factorials = [math.factorial(i) for i in range(10)]

for n in range(3, 2540160):
    sum_factorials_digits = sum([factorials[int(digit)] for digit in str(n)])

    if n == sum_factorials_digits:
        s += n

print(s)
