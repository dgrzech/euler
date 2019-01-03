import math
import tools

found = False
n = 35
primes_smaller_than_n = [i for i in range(2, n+1) if tools.is_prime(i)]
print(primes_smaller_than_n)

while not found:
    if tools.is_prime(n):
        primes_smaller_than_n.append(n)
        n += 2
        continue
    else:
        for prime in primes_smaller_than_n:
            temp = (n - prime) / 2
            temp_list = [i for i in range(1, int(math.sqrt(n) + 1)) if i ** 2 == temp]

            if len(temp_list) > 0:
                print(str(n) + ' = ' + str(prime) + ' + 2x' + str(temp_list[0]) + '^2')
                n += 2
                break
            elif prime == primes_smaller_than_n[-1] and len(temp_list) == 0:
                found = True
                print(n)
