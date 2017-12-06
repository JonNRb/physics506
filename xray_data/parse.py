import math
import sys

# lambda in angstrom
lamb = 1.5418

with open(sys.argv[1], 'r') as f:
    it = iter(f)
    next(it)
    data = [map(float, l.strip().split(',')) for l in it if l.strip()]

lattice = []
for h, k, l, n, theta in data:
    theta = math.pi * theta / 180
    a = n * lamb * math.sqrt(h**2+k**2+l**2) / 2 / math.sin(theta)
    lattice.append(a)
    print(a)

mean = sum(lattice)/len(lattice)
print('mean:', mean)

stddev = math.sqrt(sum([(x-mean)**2 for x in lattice])/(len(lattice)-1))
print('stddev:', stddev)
print('relerr:', stddev/mean)
