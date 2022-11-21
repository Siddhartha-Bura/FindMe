import matplotlib.pyplot as plt
import pandas as pd

columns_data=['time','x','y','z']
df = pd.read_csv('Standing.csv')
df=df.iloc[:,:-1]
df.columns=columns_data
df['time']=df['time']*10000
fig, ax=plt.subplots(2, 3, figsize=(15,9))
ax[0,0].plot(df['time'][:5000],df['x'][:5000], color='r',label='x_acc')
ax[0,0].plot(df['time'][:5000],df['y'][:5000], color='g',label='y_acc')
ax[0,0].plot(df['time'][:5000],df['z'][:5000], color='b',label='z_acc')
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('Acc_data')
ax[0,0].title.set_text('Standing Data')

columns_data=['time','x','y','z']
df = pd.read_csv('Sitting.csv')
df=df.iloc[:,:-1]
df.columns=columns_data
df['time']=df['time']*10000
ax[0,1].plot(df['time'][:5000],df['x'][:5000], color='r',label='x_acc')
ax[0,1].plot(df['time'][:5000],df['y'][:5000], color='g',label='y_acc')
ax[0,1].plot(df['time'][:5000],df['z'][:5000], color='b',label='z_acc')
ax[0,1].set_xlabel('Time')
ax[0,1].set_ylabel('Acc_data')
ax[0,1].title.set_text('Sitting Data')


columns_data=['time','x','y','z']
df = pd.read_csv('Lying.csv')
df=df.iloc[:,:-1]
df.columns=columns_data
df['time']=df['time']*10000
ax[0,2].plot(df['time'][:5000],df['x'][:5000], color='r',label='x_acc')
ax[0,2].plot(df['time'][:5000],df['y'][:5000], color='g',label='y_acc')
ax[0,2].plot(df['time'][:5000],df['z'][:5000], color='b',label='z_acc')
ax[0,2].set_xlabel('Time')
ax[0,2].set_ylabel('Acc_data')
ax[0,2].title.set_text('Lying Data')

columns_data=['time','x','y','z']
df = pd.read_csv('Standing_data1.txt',header=None)
df=df.iloc[:,2:]
df.columns=columns_data
df['time']=df['time'].map(lambda a:a - min(df['time']))
ax[1,0].plot(df['time'][:5000],df['x'][:5000], color='r',label='x_acc')
ax[1,0].plot(df['time'][:5000],df['y'][:5000], color='g',label='y_acc')
ax[1,0].plot(df['time'][:5000],df['z'][:5000], color='b',label='z_acc')
ax[1,0].set_xlabel('Time')
ax[1,0].set_ylabel('Acc_data')
ax[1,0].title.set_text('Standing_PhonePi')

columns_data=['time','x','y','z']
df = pd.read_csv('Sitting_data1.txt',header=None)
df=df.iloc[:,2:]
df.columns=columns_data
df['time']=df['time'].map(lambda a:a - min((df['time'])))
ax[1,1].plot(df['time'][:5000],df['x'][:5000], color='r',label='x_acc')
ax[1,1].plot(df['time'][:5000],df['y'][:5000], color='g',label='y_acc')
ax[1,1].plot(df['time'][:5000],df['z'][:5000], color='b',label='z_acc')
ax[1,1].set_xlabel('Time')
ax[1,1].set_ylabel('Acc_data')
ax[1,1].title.set_text('Sitting_PhonePi')

columns_data=['time','x','y','z']
df = pd.read_csv('Lying_data1.txt',header=None)
df=df.iloc[:,2:]
df.columns=columns_data
df['time']=df['time'].map(lambda a:a - min(df['time']))
ax[1,2].plot(df['time'][:5000],df['x'][:5000], color='r',label='x_acc')
ax[1,2].plot(df['time'][:5000],df['y'][:5000], color='g',label='y_acc')
ax[1,2].plot(df['time'][:5000],df['z'][:5000], color='b',label='z_acc')
ax[1,2].set_xlabel('Time')
ax[1,2].set_ylabel('Acc_data')
ax[1,2].title.set_text('Lying_PhonePi')

plt.legend()
plt.show()
