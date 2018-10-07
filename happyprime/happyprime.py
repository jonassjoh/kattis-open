from math import sqrt, log

def happy(m):
    if not prime(m): return "NO"
    return _happy(m, [m])

def _happy(m, v):
    if m == 1: return "YES"
    m = [int(i)**2 for i in str(m)]
    m = sum(m)
    if m in v: return "NO"
    return _happy(m, v + [m])

def prime(m):
    if m == 1: return False
    for i in range(2, int(sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True

def mul2(m):
    l = int(log(m, 2))

P = int(input())

for _ in range(P):
    l = input().split(" ")
    K = int(l[0])
    m = int(l[1])

    r = happy(m)

    print(K, m, r)
