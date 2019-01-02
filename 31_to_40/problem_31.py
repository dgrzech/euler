# denominations = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
# max_number_in_two_pounds = {denomination: 2 / denomination for denomination in denominations}
#
# print(max_number_in_two_pounds)

# count = 0
#
# for a in range(200, -1, -200):  # -1 to ensure that the interval is right-inclusive
#     for b in range(a, -1, -100):
#         for c in range(b, -1, -50):
#             for d in range(c, -1, -20):
#                 for e in range(d, -1, -10):
#                     for f in range(e, -1, -5):
#                         for g in range(f, -1, -2):
#                             count += 1
#
# print(count)

target = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]

ways = [0 for i in range(target + 1)]
ways[0] = 1

for i, coin in enumerate(denominations):
    for j in range(coin, target + 1):
        ways[j] += ways[j - coin]

print(max(ways))
