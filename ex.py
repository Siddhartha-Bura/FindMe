from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pykalman import KalmanFilter
plt.style.use('fivethirtyeight')
data_smoothened = []
def animate(i):
    df = pd.read_csv('abc.csv', header=None)
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    if (not df[0].isnull().values.any() and not not df[0].isnull().values.any()) or not predict(df):
        return
    plt.plot(df[0], df[1], marker='>', linewidth=1)
    plt.tight_layout()
    count = 1
    for x, y in zip(df[0], df[1]):
        plt.text(x, y, str(count), color="red", fontsize=12)
        count += 1

def predict(df):
    global data_smoothened
    if(df.shape[0] == len(data_smoothened)):
        return False
    data = df.to_numpy()
    ism = [data[0, 0],0,data[0, 1],0]
    tm = [[1, 1, 0, 0],[0, 1, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1]]
    om = [[1, 0, 0, 0],[0, 0, 1, 0]]
    kf1 = KalmanFilter(transition_matrices = tm,observation_matrices = om,initial_state_mean = ism)
    kf1 = kf1.em(data, n_iter=5)
    (smoothed_state_means, _ ) = kf1.smooth(data)
    plt.plot(smoothed_state_means[:, 0], smoothed_state_means[:, 2], 'r--')
    data_smoothened = smoothed_state_means 
    return True

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

