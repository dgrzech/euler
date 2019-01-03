import math

found = False
idx = 286

while not found:
    triangle = int(idx * (idx + 1) / 2)

    delta1 = 1 + 8 * triangle
    k = (1 + math.sqrt(delta1)) / 4

    if not k.is_integer():
        idx += 1
        continue

    delta2 = 1 + 24 * triangle
    l = (1 + math.sqrt(delta2)) / 6

    if not l.is_integer():
        idx += 1
        continue

    found = True
    print(triangle)
