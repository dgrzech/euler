import tools

upper_limit = 1000000
primes = tools.sieve_of_eratosthenes(upper_limit)

res = 0
count = 0

for i, prime_1 in enumerate(primes):
    temp = [prime_1]

    for prime_2 in primes[i+1:]:
        if temp[-1] + prime_2 < upper_limit:
            temp.append(temp[-1] + prime_2)
        else:
            break

    for j, p in enumerate(reversed(temp)):
        if tools.is_prime(p):
            temp = temp[:len(temp)-j]
            break

    if len(temp) > count:
        res = temp[-1]
        count = len(temp)

print(res)
print(count)
