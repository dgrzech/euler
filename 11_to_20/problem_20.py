l = [i for i in range(101)]  # list all integers from 1 to 100

# factor out the multiples of 10 to enable storing the product
for n, i in enumerate(l):
    for m, j in enumerate(l):
        if i * j % 10 == 0:
            l[n] = int(i * j / 10)
            l[m] = 1
            break

# print(l)

# calculate the product of the numbers stored in the list
product = 1
for i in l:
    product *= i

# print(product)

# calculate the sum of the digits in 100!
sum = 0
for letter in str(product):
    sum += int(letter)

print(sum)
