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

            self.middle_time_10 = np.array([self.x_time[i] for i in range(len(self.x_time)) if i % 10 == 0])
            self.middle_head_10 = self.get_middle(self.y_head, number=10, minus=5, len_time=len(self.middle_time_10))
            self.middle_pitch_10 = self.get_middle(self.y_pitch, number=10, minus=5, len_time=len(self.middle_time_10))

            self.middle_time_20 = np.array([self.x_time[i] for i in range(len(self.x_time)) if i % 20 == 0])
            self.middle_head_20 = self.get_middle(self.y_head, number=20, minus=15, len_time=len(self.middle_time_20))
            self.middle_pitch_20 = self.get_middle(self.y_pitch, number=20, minus=15, len_time=len(self.middle_time_20))

        
        def get_middle(self, array, number: int, minus: int, len_time: int):
            middle_list = []
            temp_list = []
            for i in range(len_time*number - minus):
                temp_list.append(array[i])
                if (i+1) % number == 0:
                    middle_list.append(sum(temp_list) / number)
                    temp_list.clear()
            return middle_list

        
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

        def show_middle_head_to_time_10(self) -> None:
            figure = plt.figure()
            plt.plot(self.middle_time_10[:-1], self.middle_head_10, marker='*', markerfacecolor='w')
            plt.xlabel('Час')
            plt.ylabel('Кут курсу')
            plt.suptitle('Head by time sets 10 middle')
            plt.show()
            figure.savefig('head_by_time_middle_10.jpg')
            return None

        def show_middle_pitch_to_time_10(self) -> None:
            figure = plt.figure()
            plt.plot(self.middle_time_10[:-1], self.middle_pitch_10, marker='*', markerfacecolor='w')
            plt.xlabel('Час')
            plt.ylabel('Кут крену')
            plt.suptitle('Pitch by time sets 10 middle')
            plt.show()
            figure.savefig('pitch_by_time_middle_10.jpg')
            return None

        def show_middle_head_to_time_20(self) -> None:
            figure = plt.figure()
            plt.plot(self.middle_time_20[:-1], self.middle_head_20, marker='*', markerfacecolor='w')
            plt.xlabel('Час')
            plt.ylabel('Кут курсу')
            plt.suptitle('Head by time sets 20 middle')
            plt.show()
            figure.savefig('head_by_time_middle_20.jpg')
            return None

        def show_middle_pitch_to_time_20(self) -> None:
            figure = plt.figure()
            plt.plot(self.middle_time_20[:-1], self.middle_pitch_20, marker='*', markerfacecolor='w')
            plt.xlabel('Час')
            plt.ylabel('Кут крену')
            plt.suptitle('Pitch by time sets 20 middle')
            plt.show()
            figure.savefig('pitch_by_time_middle_20.jpg')
            return None


pan = Pandas()

# pan.show.show_head_to_time()
# pan.show.show_pitch_to_time()

# pan.show.show_middle_head_to_time_10()
# pan.show.show_middle_pitch_to_time_10()

# pan.show.show_middle_head_to_time_20()
# pan.show.show_middle_pitch_to_time_20()

print(f'Середнє значення head(t): {sum(pan.show.y_head)/len(pan.show.y_head)}')
print(f'Середнє значення pitch(t): {sum(pan.show.y_pitch)/len(pan.show.y_pitch)}')

print(f'Середнє квадратичне відхилення head(t): {pan.show.y_head.std()}')
print(f'Середнє квадратичне відхилення pitch(t): {pan.show.y_pitch.std()}')

print(f'Максимальне відхилення head(t) від середнього значення: {max(pan.show.y_head) - (sum(pan.show.y_head)/len(pan.show.y_head))}')
print(f'Максимальне відхилення pitch(t) від середнього значення: {max(pan.show.y_pitch) - (sum(pan.show.y_pitch)/len(pan.show.y_pitch))}')
