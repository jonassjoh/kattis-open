from random import randint as rand
from random import sample

with open(input('Enter sample name: '), 'w') as f:
    samples = rand(0, 5)
    L = rand(1, 99999)
    A = rand(1, L + 1)
    f.write(str(L) + " " + str(A) + "\n")
    positions = []
    for i in range(A):
        p = rand(0, L)
        while p in positions:
            p = rand(0, L)
        positions.append(p)
        d = sample(['R', 'L'], 1)
        f.write(str(p) + " " + d[0])
        if i != A - 1:
            f.write('\n')
