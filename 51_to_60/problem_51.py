import tools

n = int(3*1e7)
l = tools.sieve_of_eratosthenes(n)
print('sieve finished')

for p in l:
    if p > 1000:
        s = str(p)

        if int(s[-2]) <= 1 and s[-2] == s[-3] and s[-3] == s[-4]:
            prime_digit_replacements = [p + i * 1110 for i in range(0, 10) if p + i * 1110 in l]
            if len(prime_digit_replacements) >= 8:
                print(prime_digit_replacements)

