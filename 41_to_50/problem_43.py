import tools

digits = [i for i in range(10)]
permutations = tools.permute(digits)

first_primes = [2, 3, 5, 7, 11, 13, 17]
result = []
for permutation in permutations:
    if permutation[0] != 0:
        s = ''.join(str(digit) for digit in permutation)
        substrings = [int(s[i:i+3]) for i in range(1, len(s) - 2)]

        divisible = True
        for k, substring in enumerate(substrings):
            divisible = divisible and (substring % first_primes[k] == 0)

        if divisible:
            # print(s, substrings)
            result.append(int(s))

print(sum(result))
