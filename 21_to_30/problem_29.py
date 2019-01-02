# import numpy as np
#
# a_b_min = 2
# a_b_max = 100
#
# l = []
# for a in range(a_b_min, a_b_max + 1):
#     l.append(np.ones(a_b_max - 1, dtype=int))
#
# s = sum([np.sum(b) for b in l])
# print('no. of all possible combinations: ' + str(s))
#
# for i, base_list in enumerate(l):
#     a = i + 2
#     powers_a = [a ** n for n in range(a_b_min, a_b_max + 1)]
#
#     for b in range(a + 1, a_b_max + 1):
#         powers_b = [b ** n for n in range(a_b_min, a_b_max + 1)]
#
#         for j, number in enumerate(powers_b):
#             if number in powers_a:
#                 l[b - 2][j] = 0
#
# s = sum([np.sum(b) for b in l])
# print('no. of combinations without repeating elements: ' + str(s))

print(len(set([a ** b for a in range(2, 101) for b in range(2, 101)])))
