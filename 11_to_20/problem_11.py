l = []
list = []

with open('p11_grid.txt', 'rt') as file:
    for line in file:
        line = line.split(' ')
        line[-1] = line[-1].strip()
        line = [int(el) for el in line]

        l.append(line)

print(l)

max_product = 1
max_list = []

for i in range(len(l)):  # sum of columns for a given row
    for j in range(len(l[0]) - 3):
        temp = 1
        temp_list = []

        for k in range(j, j+4):
            temp *= l[i][k]
            temp_list.append(l[i][k])

        if temp > max_product:
            max_product = temp
            max_list = temp_list


for i in range(len(l[0])):  # sum of rows for a given column
    for j in range(len(l) - 3):
        temp = 1
        temp_list = []

        for k in range(j, j+4):
            temp *= l[k][j]
            temp_list.append(l[k][j])

        if temp > max_product:
            max_product = temp
            max_list = temp_list


for i in range(len(l) - 3):  # diagonals 1
    for j in range(len(l) - 3):
        temp = 1
        temp_list = []

        for k in range(0, 4):
            temp *= l[i+k][j+k]
            temp_list.append(l[i+k][j+k])

        if temp > max_product:
            max_product = temp
            max_list = temp_list


for i in range(len(l)-4, -1, -1):  # diagonals 2
    for j in range(len(l[0])-1, 2, -1):
        temp = 1
        temp_list = []

        for k in range(0, 4):
            temp *= l[i+k][j-k]
            temp_list.append(l[i+k][j-k])

        if temp > max_product:
            max_product = temp
            max_list = temp_list


print(max_product)
print(max_list)
