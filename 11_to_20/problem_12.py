import tools

n = 1
min_no_divisors = 500


def dict_product(d):
    keys = d.keys()
    prod = 1

    for key in keys:
        prod *= (d[key] + 1)

    return prod


while True:
    triangle_no = int(n*(n+1) / 2)

    pf = tools.prime_factors(triangle_no)
    d = {x: pf.count(x) for x in pf}

    no_divisors = dict_product(d)
    if no_divisors >= min_no_divisors:
        print(triangle_no, no_divisors)
        break

    n += 1
