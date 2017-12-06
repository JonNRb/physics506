import os

xray_data_root = '../../xray_data'

csv_files = [os.path.join(xray_data_root, i)
             for i in os.listdir(xray_data_root) if i.endswith('.txt')]
csv_data = {}
for name in csv_files:
    with open(name) as f:
        it = iter(f)
        for _ in range(6):
            next(it)
        data = list(zip(*[[float(i) for i in line.strip().split('\t')]
                          for line in it if line.strip()]))
    if name.find(',') > 0:
        print('found data that has degrees attached:', name)
        a, b = map(int, name.split(',')[1].split('.')[0].split('-'))
        x_data, y_data = data
        min_t, max_t = x_data[0], x_data[-1]
        scale = (b - a) / (max_t - min_t)
        if b > a:
            offset = a * scale
        else:
            offset = -1.0 * b * scale
        x_data = [x * scale + offset for x in x_data]
        data = x_data, y_data
    csv_data[name] = data
