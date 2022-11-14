from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.app import App
from kivy.lang import Builder
from pykalman import KalmanFilter

plt.style.use('fivethirtyeight')
plt.switch_backend('agg')


class uiApp(App):
    data_smoothened = []
    kf = KalmanFilter()

    def build(self):
        self.str = Builder.load_string(""" 
BoxLayout:
    layout:layout
      
    BoxLayout:
      
        id:layout
      
                                """)

        Clock.schedule_interval(self.animate, 1)
        self.str.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return self.str

    def animate(self, i=None):
        df = pd.read_csv('abc.csv', header=None)
        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        if (not df[0].isnull().values.any() and not not df[0].isnull().values.any()) or not self.predict(df):
            return
        self.str.layout.clear_widgets()

        plt.plot(df[0], df[1], marker='>', linewidth=1)
        plt.tight_layout()
        count = 1
        for x, y in zip(df[0], df[1]):
            plt.text(x, y, str(count), color="red", fontsize=12)
            count += 1
        canvas = FigureCanvasKivyAgg(plt.gcf())
        self.str.layout.add_widget(canvas)
        canvas.draw()

    def predict(self,df):
        if(df.shape[0] == len(self.data_smoothened)):
            return False
        data = df.to_numpy()
        ism = [data[0, 0],0,data[0, 1],0]
        tm = [[1, 1, 0, 0],[0, 1, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1]]
        om = [[1, 0, 0, 0],[0, 0, 1, 0]]
        kf1 = KalmanFilter(transition_matrices = tm,observation_matrices = om,initial_state_mean = ism)
        kf1 = kf1.em(data, n_iter=5)
        (smoothed_state_means, _) = kf1.smooth(data)
        plt.plot(smoothed_state_means[:,0], smoothed_state_means[:, 2], 'r--')
        return True

if __name__ == '__main__':
    uiApp().run()
