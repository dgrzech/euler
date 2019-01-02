import numpy as np


def sum_of_squares(n):
    squares = np.arange(n + 1) * np.arange(n + 1)
    return np.sum(squares)


def square_of_sum(n):
    return (n ** 2) * (n + 1) ** 2 / 4


n = 100
print(square_of_sum(n) - sum_of_squares(n))
