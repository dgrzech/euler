import tools.py as tools

count = 0
truncatable_primes = []

curr = 11
while count < 11:
    all_truncations_primes = True

    truncations_left = [int(str(curr)[i:]) for i in range(len(str(curr)))]
    for truncation in truncations_left:
        all_truncations_primes = all_truncations_primes and tools.is_prime(truncation)

        if not all_truncations_primes:
            break

    if not all_truncations_primes:
        curr += 1
        continue

    truncations_right = [int(str(curr)[:i+1]) for i in range(len(str(curr)))]
    for truncation in truncations_right:
        all_truncations_primes = all_truncations_primes and tools.is_prime(truncation)

        if not all_truncations_primes:
            break

    if all_truncations_primes:
        truncatable_primes.append(curr)
        count += 1
        curr += 1
    else:
        curr += 1

print(truncatable_primes)
print(sum(truncatable_primes))
