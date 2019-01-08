import tools

upper_bound = 2000001
primes = tools.sieve_of_eratosthenes(upper_bound)

print(sum(primes))
