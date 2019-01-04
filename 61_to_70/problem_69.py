import tools

upper_bound = 1000000
primes_under_upper_bound = tools.sieve_of_eratosthenes(upper_bound)  # sieve of eratosthenes for quickly computing all primes under upper bound
print(primes_under_upper_bound)

#
# def calc_euler_totient(n):  # using euler's product formula
#     divisor_primes_smaller_than_n = [i for i in primes_under_upper_bound if i <= n and n % i == 0]
#     product = n
#     for i in divisor_primes_smaller_than_n:
#         product *= (1 - 1 / i)
#
#     return product
#
#
# euler_totients = [0] * (upper_bound+1)
# for i in range(1, len(euler_totients)):
#     if i % 10000 == 0:
#         print(i)
#
#     if euler_totients[i] != 0:
#         continue
#     elif euler_totients[i] == 0 and i in primes_under_upper_bound:
#         temp = i
#         while temp <= upper_bound:
#             euler_totients[temp] = temp * (1 - 1/i)
#             temp *= i
#     else:
#         euler_totients[i] = calc_euler_totient(i)
#
#
# max_n_phi_n = 0
# max_n = 0
#
# for i in range(2, upper_bound+1):
#     if i / euler_totients[i] > max_n_phi_n:
#         max_n_phi_n = i / euler_totients[i]
#         max_n = i
#
#
# print(max_n, max_n_phi_n)

n = 1
i = 0

while n * primes_under_upper_bound[i] < upper_bound:
    n *= primes_under_upper_bound[i]
    i += 1

print(n)
