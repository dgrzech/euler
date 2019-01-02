import tools

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = tools.permute(digits)

pandigital_products = []
for permutation in permutations:
    s = ''.join(str(e) for e in permutation)

    for idx_1 in range(len(s) - 2):
        for idx_2 in range(idx_1 + 2, len(s)):
            multiplicand = int(s[:idx_1 + 1])
            multiplier = int(s[idx_1 + 1:idx_2])
            product = int(s[idx_2:])

            if multiplicand * multiplier == product:
                pandigital_products.append([multiplicand, multiplier, product])

print('pandigital products: ', pandigital_products)

pandigital_products_no_duplicates = []
for pandigital_product in pandigital_products:
    if pandigital_product[2] not in pandigital_products_no_duplicates:
        pandigital_products_no_duplicates.append(pandigital_product[2])

print('pandigital products with no duplicates: ', pandigital_products_no_duplicates)
print('sum of pandigital products: ', sum(pandigital_products_no_duplicates))
