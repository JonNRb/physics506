import os

zeeman_data_root = '../../zeeman_data'

csv_files = [os.path.join(zeeman_data_root, i)
             for i in os.listdir(zeeman_data_root) if i.endswith('.csv')]
csv_data = {}
for name in csv_files:
    with open(name) as f:
        data = list(zip(*[[float(i) for i in line.strip().split(',')]
                          for line in f if line.strip()]))
    csv_data[name] = data

field_map = {1.0: 0.239, 2.0: 0.417, 3.0: 0.566, 4.0: 0.755,
             5.0: 0.902, 6.0: 1.015, 7.0: 1.211, 8.0: 1.256,
             9.0: 1.275, 10.0: 1.295}
points_files = [os.path.join(zeeman_data_root, i)
                for i in os.listdir(zeeman_data_root) if i.endswith('_points.txt')]
points_data = {}
for i in points_files:
    data = []
    with open(i) as f:
        it = iter(f)
        while True:
            x = next(it)
            if x[0] == '-':
                x = float(next(it))
                # adjust to (delta lambda) / (lambda^2). divide by 2 because
                # the `diff` is double the split (peak to peak after split)
                data = [(field_map[j[0]], 0.5 * j[1] / (x*x)) for j in data]
                break
            data.append([float(j) for j in x.split(',')])
    points_data[i] = data
