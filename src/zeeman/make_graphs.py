import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import data
import regression


def scientific_notation(value):
    if value == 0:
        return '0'
    else:
        e = np.log10(np.abs(value))
        m = np.sign(value) * 10 ** (e - int(e))
        return r'${:.1f} \cdot 10^{{{:d}}}$'.format(m, int(e))


scientific_formatter = mpl.ticker.FuncFormatter(
    lambda x, p: scientific_notation(x))
identity_formatter = mpl.ticker.FuncFormatter(lambda x, p: r'${0}$'.format(x))

for name, data_item in data.csv_data.items():
    print(name)

    plt.figure(figsize=(800 / 96, 600 / 96))
    plt.plot(data_item[0], data_item[1], 'bo', linewidth=2.0)
    plt.axis('auto')
    plt.ylabel('Counts Per Second')
    plt.xlabel('Wavelength (nm)')
    plt.gca().xaxis.set_major_formatter(identity_formatter)
    plt.gca().yaxis.set_major_formatter(scientific_formatter)
    plt.savefig(name.replace('csv', 'png'), dpi=240,
                bbox_inches='tight', transparent=True)
    plt.clf()

for name, d in data.points_data.items():
    print(name)
    slope, intercept, std_err = regression.regress(d)

    plt.figure(figsize=(800 / 96, 600 / 96))

    x, y = zip(*d)
    plt.plot(x, y, 'bo', linewidth=2.0)

    def f(x): return intercept + slope * x
    f_x = np.arange(min(x), max(x), 0.001)
    plt.plot(f_x, f(f_x), 'r-', linewidth=1.0)

    plt.errorbar(x, [f(i) for i in x], fmt='r-', yerr=[std_err/2] * len(x))

    plt.axis('auto')
    plt.ylabel('$\Delta\lambda / \lambda^2$ (1/nm)')
    plt.xlabel('Magnetic Field Strength (T)')
    plt.gca().xaxis.set_major_formatter(identity_formatter)
    plt.gca().yaxis.set_major_formatter(scientific_formatter)
    plt.savefig(name.replace('txt', 'png'), dpi=240,
                bbox_inches='tight', transparent=True)
    plt.clf()
