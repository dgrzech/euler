import itertools
import tools

found = False
i = 125874

while not found:
    if i % 1000 == 0:
        print(i)

    permutations = set(itertools.permutations([letter for letter in str(i)]))
    if tuple(str(i * 2)) in permutations and tuple(str(i * 3)) in permutations and tuple(str(i * 4)) in permutations and tuple(str(i * 5)) in permutations and tuple(str(i * 6)) in permutations:
        found = True
        print(i)
    else:
        i += 1
