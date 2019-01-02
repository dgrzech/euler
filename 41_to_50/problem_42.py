import math
import string


def is_triangle(n):
    delta = 1 + 8 * n
    n1 = (-1 - math.sqrt(delta)) / 2
    n2 = (-1 + math.sqrt(delta)) / 2

    return (n1 > 0 and n1.is_integer()) or (n2 > 0 and n2.is_integer())


triangle_words = []
with open('p042_words.txt') as file:
    for line in file:
        line = line.split(',')
        for word in line:
            word_value = sum([string.ascii_uppercase.index(character) + 1 for character in word.strip('\"')])

            if is_triangle(word_value):
                triangle_words.append(word)

print(triangle_words)
print(len(triangle_words))
