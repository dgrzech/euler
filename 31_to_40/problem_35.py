import tools.py as tools

n = [i for i in range(2, int(1e6))]

non_prime_digits = ['0', '2', '4', '5', '6', '8']
circular_primes = ['2', '5']
for number in n:
    if number % 2 == 1:  # check that the number is odd

        has_non_prime_digits = False  # check that the number has no digits that would make one of its rotations non-prime
        for digit in non_prime_digits:
            if digit in str(number):
                has_non_prime_digits = True
                break

        if not has_non_prime_digits:
            number_rotations = tools.rotations(str(number))
            all_rotations_prime = True

            for rotation in number_rotations:
                if not tools.is_prime(int(rotation)):
                    all_rotations_prime = False
                    break

            if all_rotations_prime:
                circular_primes.append(number)

print(circular_primes)
print(len(circular_primes))
