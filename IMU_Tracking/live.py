from mimetypes import init
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from scipy import integrate

ax_new = []
ay_new = []
az_new = []

def animate(i):
    data = pd.read_csv('acceleration.csv', header=None)
    # gyro = pd.read_csv('gyroscope.csv', header=None)

    t = data[0]
    # t1 = data[2][data[2].size-1]
    # t2 = data[3][data[3].size-1]
    # t3 = data[1][data[1].size-1]
    t1 = data[2]
    t2 = data[3]
    t3 = data[1]
    ax = data[4]
    ay = data[5]
    az = data[6]


    R = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # R[0][0] = np.cos(t2*(np.pi/180))*np.cos(t3*(np.pi/180))
    # R[0][1] = np.sin(t1*(np.pi/180))*np.sin(t2*(np.pi/180))*np.cos(t3*(np.pi/180)) - np.cos(t1*(np.pi/180))*np.sin(t3*(np.pi/180))
    # R[0][2] = np.cos(t1*(np.pi/180))*np.sin(t2*(np.pi/180))*np.cos(t3*(np.pi/180)) + np.sin(t1*(np.pi/180))*np.cos(t3*(np.pi/180))
    # R[1][0] = np.cos(t2*(np.pi/180))*np.sin(t3*(np.pi/180))
    # R[1][1] = np.sin(t1*(np.pi/180))*np.sin(t2*(np.pi/180))*np.sin(t3*(np.pi/180)) + np.cos(t1*(np.pi/180))*np.cos(t3*(np.pi/180))
    # R[1][2] = np.cos(t1*(np.pi/180))*np.sin(t2*(np.pi/180))*np.sin(t3*(np.pi/180)) - np.sin(t1*(np.pi/180))*np.cos(t3*(np.pi/180))
    # R[2][0] = -np.sin(t2*(np.pi/180))
    # R[2][1] = np.sin(t1*(np.pi/180))*np.cos(t2*(np.pi/180))
    # R[2][2] = np.cos(t1*(np.pi/180))*np.cos(t2*(np.pi/180))
    R[0][0] = np.cos(t2[t2.size-1]*(np.pi/180))*np.cos(t3[t3.size-1]*(np.pi/180))
    R[0][1] = np.sin(t1[t1.size-1]*(np.pi/180))*np.sin(t2[t2.size-1]*(np.pi/180))*np.cos(t3[t3.size-1]*(np.pi/180)) - np.cos(t1[t1.size-1]*(np.pi/180))*np.sin(t3[t3.size-1]*(np.pi/180))
    R[0][2] = np.cos(t1[t1.size-1]*(np.pi/180))*np.sin(t2[t2.size-1]*(np.pi/180))*np.cos(t3[t3.size-1]*(np.pi/180)) + np.sin(t1[t1.size-1]*(np.pi/180))*np.cos(t3[t3.size-1]*(np.pi/180))
    R[1][0] = np.cos(t2[t2.size-1]*(np.pi/180))*np.sin(t3[t3.size-1]*(np.pi/180))
    R[1][1] = np.sin(t1[t1.size-1]*(np.pi/180))*np.sin(t2[t2.size-1]*(np.pi/180))*np.sin(t3[t3.size-1]*(np.pi/180)) + np.cos(t1[t1.size-1]*(np.pi/180))*np.cos(t3[t3.size-1]*(np.pi/180))
    R[1][2] = np.cos(t1[t1.size-1]*(np.pi/180))*np.sin(t2[t2.size-1]*(np.pi/180))*np.sin(t3[t3.size-1]*(np.pi/180)) - np.sin(t1[t1.size-1]*(np.pi/180))*np.cos(t3[t3.size-1]*(np.pi/180))
    R[2][0] = -np.sin(t2[t2.size-1]*(np.pi/180))
    R[2][1] = np.sin(t1[t1.size-1]*(np.pi/180))*np.cos(t2[t2.size-1]*(np.pi/180))
    R[2][2] = np.cos(t1[t1.size-1]*(np.pi/180))*np.cos(t2[t2.size-1]*(np.pi/180))

    acc = [ax[ax.size-1],ay[ay.size-1],az[az.size-1]]

    acc3d = np.matmul(R, acc)
    # acc3d = np.matmul(np.transpose(R), acc)
    ax_new.append(acc3d[0])
    ay_new.append(acc3d[1])
    az_new.append(acc3d[2])


    # with open('dummy.txt', 'a') as csv_file:
    #     print(R, file=open('dummy.txt', 'a'))

    vx = [0]
    vy = [0]
    vz = [0]

    for i in range(len(ax_new)-1): 
        # vx = vx + [vx[-1] + ax[i]*(t[i+1]-t[i])/1000]
        # vy = vy + [vy[-1] + ay[i]*(t[i+1]-t[i])/1000]
        # vz = vz + [vz[-1] + az[i]*(t[i+1]-t[i])/1000]
        vx = vx + [vx[-1] + ax_new[i]*0.1]
        vy = vy + [vy[-1] + ay_new[i]*0.1]
        vz = vz + [vz[-1] + az_new[i]*0.1]
    
    x = [0]
    y = [0]
    z = [0]

    for i in range(len(ax_new)-1): 
        # x = x + [x[-1] + vx[i]*(t[i+1]-t[i])/1000]
        # y = y + [y[-1] + vy[i]*(t[i+1]-t[i])/1000]
        # z = z + [z[-1] + vz[i]*(t[i+1]-t[i])/1000]
        x = x + [x[-1] + vx[i]*0.1]
        y = y + [y[-1] + vy[i]*0.1]
        z = z + [z[-1] + vz[i]*0.1]

    plt.cla()
    plt.grid()
    
    img = plt.imread("boundary.jpg")
    plt.imshow(img, extent=[-100, 100, 100, -100])

    plt.plot(x,y, label='xy')
    # plt.plot(ax_new,ay_new, label='xy')
    if (x[-1]*x[-1] + y[-1]*y[-1] > 10000):
        print("Outside")

    plt.xlim(-100, 100)
    plt.ylim(-100, 100)   

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
