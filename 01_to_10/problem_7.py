import numpy as np
import tools

n = 10001

lower_bound = n * np.log(n) + n * (np.log(np.log(n)) - 1)
upper_bound = n * np.log(n) + n * np.log(np.log(n))

print(lower_bound)
print(upper_bound)

primes = tools.sieve_of_eratosthenes(int(upper_bound))
print(len(primes))
print(primes[10000])

