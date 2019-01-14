n = 10000
l = [0 for i in range(n+1)]

for i in range(len(l)):
    for potential_divisor in range(1, int(i/2)+1):
        if i % potential_divisor == 0:
            l[i] += potential_divisor

s = 0
for k in range(len(l)):
    if l[k] < len(l) and k != l[k] and l[l[k]] == k:
        s += k

print(s)
