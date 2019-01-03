digit_cancelling_fractions = []

for i in range(10, 100):
    for j in range(10, 100):
        fraction = i / j
        if fraction >= 1 or i % 10 == 0 or j % 10 == 0 or i == j:
            continue

        i_str = str(i)
        j_str = str(j)

        letters = [letter for letter in i_str if letter in j_str]
        if i_str[0] == j_str[0] or i_str[1] == j_str[1] or len(letters) != 1:
            continue

        letter = letters[0]
        str_1 = i_str.replace(letter, '')
        str_2 = j_str.replace(letter, '')

        if int(str_1) / int(str_2) == fraction:
            digit_cancelling_fractions.append([i, j])
            # digit_cancelling_fractions.append(fraction)

print(digit_cancelling_fractions)
