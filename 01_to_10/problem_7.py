import numpy as np

n = 10001

lower_bound = n * np.log(n) + n * (np.log(np.log(n)) - 1)
upper_bound = n * np.log(n) + n * np.log(np.log(n))

print(lower_bound)
print(upper_bound)

# limits = np.arange(int(lower_bound) + 1, int(upper_bound), 1)
# print(limits)
#
# no_primes = 0
# for k in limits:
#     for d in range(2, int(np.sqrt(upper_bound))):
#         if k % d == 0:
#             break
#         elif d == int(np.sqrt(upper_bound)) - 1:
#             no_primes += 1
#             print(k)
#
# print(no_primes)

