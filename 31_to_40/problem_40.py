list_integers = [i for i in range(1000001)]
n = ''.join(str(e) for e in list_integers)

idx = [int(10 ** i) for i in range(7)]
digits = [n[i] for i in idx]

result = 1
for digit in digits:
    result *= int(digit)

print(result)

