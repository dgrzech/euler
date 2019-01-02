import tools.py as tools

result = 0
for n in range(1, int(1e6)):
    n_2 = bin(n)[2:]
    if tools.is_palindromic(n) and tools.is_palindromic(n_2):
        result += n

print(result)
