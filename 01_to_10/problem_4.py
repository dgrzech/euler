import tools.py as tools

for n in range(998001, 100000, -1):  # 6-digit numbers
    if tools.is_palindromic(n):
        for d in range(100, 1000):
            if n % d == 0 and 100 <= int(n / d) < 1000:
                print(n, d, int(n / d))
                break
