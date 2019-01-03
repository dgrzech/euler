upper_limit = 354294
digit_fifth_powers = []

for i in range(2, upper_limit + 1):
    i_str = str(i)

    sum_fifth_powers_of_digits = 0
    for letter in i_str:
        sum_fifth_powers_of_digits += int(letter) ** 5

    if sum_fifth_powers_of_digits == i:
        digit_fifth_powers.append(i)

print(digit_fifth_powers)
print(sum(digit_fifth_powers))

