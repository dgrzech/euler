def collatz(n):
    if n % 2 == 0:
        return int(n / 2)

    return int(3 * n + 1)


start = 3
seq = []

for i in range(3, int(1e6), 2):  # can't skip even numbers..
    aux_start = i
    aux_seq = [i]

    while aux_seq[-1] != 1:
        aux_seq.append(collatz(aux_seq[-1]))

    if len(aux_seq) > len(seq):
        start = aux_start
        seq = aux_seq

print(start)
print(seq)
