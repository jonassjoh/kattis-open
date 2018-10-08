while True:
    N = int(input())
    if N == 0:
        break

    P = [int(i) for i in input().split(" ")]

    X, Y = [int(i) for i in input().split(" ")]

    r = []
    for i in range(X, Y + 1):
        _i = i
        for _p in P:
            while _i % _p == 0:
                _i = int(_i / _p)
        if _i == 1:
            r.append(i)

    if r == []:
        print("none")
    else:
        print(','.join(sorted([str(i) for i in r])))
