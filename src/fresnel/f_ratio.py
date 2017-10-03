txt = None
with open('f_data.txt') as f:
  txt = f.read()

lines = [i for i in txt.split('\n') if i]

data = [[int(i.strip()) for i in j.split('\t')] for j in lines]

import math

d2r = lambda ang: ang * math.pi / 180

ratio = lambda ang_2, ang_1: math.sin(d2r(ang_1)) / math.sin(d2r(ang_2))

for point in data:
  print(ratio(*point))

print('avg:', sum(ratio(*point) for point in data) / len(lines))
