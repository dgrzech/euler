def no_lattice_paths(i, j, i_max, j_max):
    count = 0

    if i == i_max or j == j_max:
        return 1

    if i < i_max:
        aux_count = no_lattice_paths(i + 1, j, i_max, j_max)
        count += aux_count
    if j < j_max:
        aux_count = no_lattice_paths(i, j + 1, i_max, j_max)
        count += aux_count

    return count


print(no_lattice_paths(0, 0, 2, 3))

# MUCH BETTER: count 40_C_20
