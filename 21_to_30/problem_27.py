import tools


def f(n, a, b):
    return n ** 2 + a * n + b


primes_under_1000 = tools.sieve_of_eratosthenes(int(1e3))

consecutive_primes = []
a_max = 0
b_max = 0

for b in primes_under_1000:
    for a in range(-b-1, 1000):
            if tools.is_prime(1 + a + b):
                temp = []
                n = 0
                while tools.is_prime(f(n, a, b)):
                    temp.append(f(n, a, b))
                    n += 1

                if len(temp) > len(consecutive_primes):
                    consecutive_primes = temp
                    a_max = a
                    b_max = b


print(a_max, b_max)
print(a_max * b_max)
print(consecutive_primes)
print(len(consecutive_primes))
