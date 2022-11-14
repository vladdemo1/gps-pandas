"""
In this mod search main info about gps data
"""
import pandas
import numpy as np
import matplotlib.pyplot as plt

from message import MESSAGE, COLUMNS


class Data:

    def __init__(self, message) -> None:
        self._message = message
        self.normal_list = []
        self._get_normal_list()

    def _get_normal_list(self) -> None:
        temp = []
        for line in self._message:
            for element in line.split(','):
                temp.append(element)
            self.normal_list.append(temp)
            temp = []
        return None


class Pandas:

    def __init__(self) -> None:
        self.df = pandas.DataFrame(data=Data(MESSAGE).normal_list, columns=COLUMNS)
        self.df_time = pandas.DataFrame(data=Data(self.df['Time']).normal_list, columns=['Time']) 
        self.df_head_t = pandas.DataFrame(data=Data(self.df['head(t)']).normal_list, columns=['head(t)'])  
        self.df_pitch_t = pandas.DataFrame(data=Data(self.df['pitch(t)']).normal_list, columns=['pitch(t)'])
        self.show = self.Show(self.df_time, self.df_head_t, self.df_pitch_t)

    class Show:

        def __init__(self, pandas_time, pandas_head, pandas_pitch) -> None:
            self.x_time = np.array([float(element) for element in pandas_time['Time']])
            self.y_head = np.array([float(element) for element in pandas_head['head(t)']])
            self.y_pitch = np.array([float(element) for element in pandas_pitch['pitch(t)']])

            self.middle_time = np.array([self.x_time[i] for i in range(len(self.x_time)) if i % 10 == 0])

        
        def show_head_to_time(self) -> None:
            figure = plt.figure()
            plt.plot(self.x_time, self.y_head, marker='*', markerfacecolor='w')
            plt.xlabel('Час')
            plt.ylabel('Кут курсу')
            plt.suptitle('Head by time')
            plt.show()
            figure.savefig('head_by_time.jpg')
            return None

        def show_pitch_to_time(self) -> None:
            figure = plt.figure()
            plt.plot(self.x_time, self.y_pitch, marker='*', markerfacecolor='w')
            plt.xlabel('Час')
            plt.ylabel('Кут крену')
            plt.suptitle('Pitch by time')
            plt.show()
            figure.savefig('pitch_by_time.jpg')
            return None

    



pan = Pandas()

# print(pan.df_time)
# print(pan.df_head_t)
# print(pan.df_pitch_t)

# print(df['Time'][0])

# pan.df.plot(kind='scatter', x='Time', y='head(t)', color='red', marker='*')
# plt.show()

# pan.df.plot(kind='scatter', x='Time', y='pitch(t)', color='red', marker='*')
# plt.show()


# print(pan.df_time)

pan.show.show_head_to_time()
pan.show.show_pitch_to_time()


# print(pan.show.middle_pitch)
