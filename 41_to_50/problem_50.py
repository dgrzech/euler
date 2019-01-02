import tools

upper_limit = 100

l = [i for i in range(2, 101)]
primes = [i for i in range(2, 101) if tools.is_prime(i)]

print(primes)
