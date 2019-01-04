import math


def is_palindromic(n):
    s = str(n)

    for i in range(int(len(s) / 2)):
        if s[i] != s[-1-i]:
            return False

    return True


def is_pandigital(number_string):
    if len(number_string) != 9:
        return False

    for digit in [str(i) for i in range(1, 10)]:
        if digit not in number_string:
            return False

    return True


def is_prime(number):
    if number == 2:
        return True

    if number % 2 == 0:
        return False
    else:
        for k in range(3, int(math.sqrt(number) + 1), 2):
            if number % k == 0:
                return False

    return True


def permute(l):
    permutations = []

    if len(l) == 1:
        permutations.append(l)
        return permutations
    elif len(l) == 2:
        permutations.append(l)
        permutations.append([l[1], l[0]])
        return permutations
    else:
        for element in l:
            temp = [el for el in l if el != element]
            temp_permutations = permute(temp)

            for permutation in temp_permutations:
                permutations.append([element] + permutation)

    return permutations


def prime_factors(n):
    i = 2
    factors = []
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors


def rotations(n):
    return [n[i:] + n[:i] for i in range(len(n))]


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if primes[i]:
            temp = [i ** 2]
            while temp[-1] + i <= n:
                temp.append(temp[-1] + i)

            for j in temp:
                primes[j] = False

    return [i for i in range(len(primes)) if primes[i]]
