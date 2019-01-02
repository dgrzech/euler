import tools

four_distinct_prime_factors = False
n1 = 647

while not four_distinct_prime_factors:
    n2 = n1 + 1
    n3 = n2 + 1
    n4 = n3 + 1

    n1_prime_factors = tools.prime_factors(n1)
    if len(set(n1_prime_factors)) == 4:
        n2_prime_factors = tools.prime_factors(n2)
        if len(set(n2_prime_factors)) == 4:
            n3_prime_factors = tools.prime_factors(n3)
            if len(set(n3_prime_factors)) == 4:
                n4_prime_factors = tools.prime_factors(n4)
                if len(set(n4_prime_factors)) == 4:
                    four_distinct_prime_factors = True
                    print(n1, n2, n3, n4)
                else:
                    n1 = n4 + 1
            else:
                n1 = n3 + 1
        else:
            n1 = n2 + 1
    else:
        n1 = n1 + 1
