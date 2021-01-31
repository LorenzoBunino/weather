# Class containing weather data from a whole month

import pandas as pd

import WeatherDay


class WeatherMonth:
    def __init__(self, rawdata):
        self.rawdata = pd.read_table(rawdata, sep=r'\s+')

    def getday(self, day):  # greedy, in a way: no permanent WeatherDay list
        max_t = self.rawdata.loc[self.rawdata['Dy'] == day, 'MxT']
        min_t = self.rawdata.loc[self.rawdata['Dy'] == day, 'MnT']
        return WeatherDay.WeatherDay(day, max_t, min_t)
