import data
import regression


for i, [x, y] in data.csv_data.items():
    assert len(x) == len(y)

    print(i)

    d = list(zip(x, y))

    m = sum([m * n for m, n in d]) / sum([n for _, n in d])
    print('mean:', m)

    mi = min(y)
    r = max(y) - min(y)

    sr = set()
    s = len(x) // 10
    for n in range(len(d) - s):
        si = max(d[n:n + s], key=lambda a: a[1])
        if si[1] > mi + 0.75 * r:
            sr.add(si)

    if i.find('zero') < 0:
        left = set()
        right = set()
        for si in sr:
            if si[0] < m:
                left.add(si)
            else:
                right.add(si)
        lm = max(left, key=lambda a: a[1])
        rm = max(right, key=lambda a: a[1])
        print('diff:', rm[0] - lm[0])
        print('{}\t{}'.format(lm[0], mi + r / 2))
        print('{}\t{}'.format(rm[0], mi + r / 2))

    print()

for name, d in data.points_data.items():
    print(name)
    slope, intercept, std_err = regression.regress(d)
    n = 4.668e-8
    print('error:', std_err)
    print('slope:', slope)
    print('g_err:', std_err / n)
    print('g:', slope / n)
    print()
