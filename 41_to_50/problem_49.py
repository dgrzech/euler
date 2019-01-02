import itertools
import tools

four_digit_primes = []
for n in range(1001, 9999, 2):
    if tools.is_prime(n):
        four_digit_primes.append(n)

print(four_digit_primes)

for prime_1 in four_digit_primes:
    permutations_str = list(itertools.permutations([e for e in str(prime_1)]))
    permutations = []

    for permutation in permutations_str:
        permutations.append(int(''.join(e for e in permutation)))

    for prime_2 in list((set(four_digit_primes) & set(permutations)) - set([prime_1])):
        for prime_3 in list((set(four_digit_primes) & set(permutations)) - set([prime_1, prime_2])):
            if abs(prime_1 - prime_2) == abs(prime_2 - prime_3) or abs(prime_1 - prime_2) == abs(prime_1 - prime_3) or abs(prime_1 - prime_3) == abs(prime_2 - 3):
                print(prime_1, prime_2, prime_3)

