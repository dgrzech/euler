def comb(n, k):
    result = 1
    for i in range(n-k+1,n+1):
        result *= i
    for i in range(1,k+1):
        result /= i

    return result

count = 0
for n in range(1,101):
    for k in range(1,int(n/2)+1):
        if comb(n,k) > int(1e6) and k < n/2:
            count += 2
        elif comb(n,k) > int(1e6) and k == n/2:
            count += 1

print(count)
