s = 100
positive_integers_under_100 = [i for i in range(1, 100)]

ways = [0 for i in range(s+1)]
ways[0] = 1

for i, integer in enumerate(positive_integers_under_100):
    for j in range(integer, s+1):
        ways[j] += ways[j - integer]

print(ways)
