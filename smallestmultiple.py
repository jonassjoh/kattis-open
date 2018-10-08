from sys import stdin
from functools import reduce
from math import sqrt

def next_prime(p):
    if p < 2: return 2
    if p == 2: return 3
    while True:
        p = p + 2
        d = True
        for i in range(2, int(sqrt(p))):
            if p % i == 0:
                d = False
                break
        if d:
            return p

def reduce_table(nr):
    p = 1
    m = []
    while True:
        done = True
        found = True
        p = next_prime(p)
        while found:
            found = False
            for i in range(len(nr)):
                if nr[i] % p == 0:
                    found = True
                    nr[i] = int(nr[i] / p)
                if nr[i] != 1:
                    done = False
            if found:
                m.append(p)
        if done:
            break
    print(m)
    return m

for line in stdin:
    nr = sorted([int(n) for n in line.split(" ")])
    primes = reduce_table(nr)
    print(reduce(lambda x, y: x*y, primes))
