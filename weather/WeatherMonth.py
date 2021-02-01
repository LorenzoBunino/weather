# Class containing weather data from a whole month

import calendar

import pandas as pd

import WeatherDay


class WeatherMonth:
    def __init__(self, rawdata, year, month):
        self.rawdata = pd.read_fwf(rawdata, widths=[5, 6, 6, 6, 7, 5, 5, 6, 7, 5, 5, 4, 4, 5, 4, 3, 6])
        self.year = year
        self.month = month

    def getday(self, day):  # greedy, in a way: no permanent WeatherDay list
        max_t = self.rawdata.loc[self.rawdata['Dy'] == day, 'MxT'].values[0]
        min_t = self.rawdata.loc[self.rawdata['Dy'] == day, 'MnT'].values[0]
        return WeatherDay.WeatherDay(self.year, self.month, day, max_t, min_t)

    def getminexcursionday(self):
        ndays = calendar.monthrange(self.year, self.month)[1]
        minexcursionday = self.getday('1')
        for day in range(2, ndays + 1):
            currentday = self.getday(str(day))
            if currentday.getexcursion() < minexcursionday.getexcursion():
                minexcursionday = currentday

        return minexcursionday
