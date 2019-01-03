import tools


def euler_totient(n):
    relative_primes = [1]

    for integer in range(2, n):
        for factor in range(2, integer + 1):
            if n % factor == 0 and integer % factor == 0:
                break
            elif (n % factor != 0 or integer % factor != 0) and factor == integer:
                relative_primes.append(integer)

    # print(n, relative_primes)
    return n / len(relative_primes)


no = 0
totient_max = 0
upper_bound = 1000000

for k in range(2, upper_bound + 1):
    temp = euler_totient(k)
    if temp > totient_max:
        no = k
        totient_max = temp

    if k % 1000 == 0:
        print(k)

print(no, totient_max)
