"""
In this mod search main info about gps data
"""
import pandas

from message import MESSAGE, COLUMNS


class Data:

    def __init__(self, message) -> None:
        self._message = message
        self.normal_list = []
        self.get_normal_list()

    def get_normal_list(self) -> None:
        temp = []
        for line in self._message:
            for element in line.split(','):
                temp.append(element)
            self.normal_list.append(temp)
            temp = []
        return None


class Pandas:

    def __init__(self) -> None:
        self._df = pandas.DataFrame(data=Data(MESSAGE).normal_list, columns=COLUMNS)
        self.df_time = self._df['Time']
        self.df_head_t = self._df['head(t)']
        self.df_pitch_t = self._df['pitch(t)']

    
pan = Pandas()

print(pan.df_time)
print(pan.df_head_t)
print(pan.df_pitch_t)
# print(df['Time'][0])
