import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import data


identity_formatter = mpl.ticker.FuncFormatter(lambda x, p: r'${0}$'.format(x))

for name, data_item in data.csv_data.items():
    print(name)

    plt.figure(figsize=(800 / 96, 600 / 96))
    plt.plot(data_item[0], data_item[1], 'b-', linewidth=0.5)
    plt.axis('auto')
    plt.ylabel('Counts Per Second')
    plt.xlabel('Minutes')
    plt.gca().xaxis.set_major_formatter(identity_formatter)
    plt.gca().yaxis.set_major_formatter(identity_formatter)
    plt.savefig(name.replace('txt', 'png'), dpi=240,
                bbox_inches='tight', transparent=True)
    plt.clf()

