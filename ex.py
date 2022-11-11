from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

def animate(i):
    df = pd.read_csv('abc.csv', header=None)
    if not df[0].isnull().values.any() and not not df[0].isnull().values.any():
        return
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.plot(df[0], df[1], marker='>', linewidth=1)
    count = 1
    for x, y in zip(df[0], df[1]):
        plt.text(x, y, str(count), color="red", fontsize=12)
        count += 1

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

