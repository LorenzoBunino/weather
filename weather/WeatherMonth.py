# Class containing weather data from a whole month

import calendar

import pandas as pd

from weather import WeatherDay


class IllegalWeatherMonth(Exception):
    pass


class WeatherMonth:
    columns = [
        'Dy',
        'MxT',
        'MnT',
        'AvT',
        'HDDay',
        'AvDP',
        '1HrP',
        'TPcpn',
        'WxType',
        'PDir',
        'AvSp',
        'Dir',
        'MxS',
        'SkyC',
        'MxR',
        'MnR',
        'AvSLP'
    ]

    def __init__(self, rawdata, year: str, month: str):
        # could also pre-pad last column with spaces instead of specifying widths
        self.rawdata = pd.read_fwf(rawdata, widths=[5, 6, 6, 6, 7, 5, 5, 6, 7, 5, 5, 4, 4, 5, 4, 3, 6])
        if self.rawdata.columns.values.tolist() != WeatherMonth.columns:
            raise IllegalWeatherMonth('Unexpected table content')
        self.year = int(year)
        self.month = int(month)
        self.ndays = calendar.monthrange(self.year, self.month)[1]

    def getday(self, day: str):  # greedy, in a way: no permanent WeatherDay list
        day_i = int(day)
        if day_i < 1 or day_i > self.ndays:
            raise ValueError('%d is out of [1, %d]', day_i, self.ndays)

        max_t = self.rawdata.loc[self.rawdata['Dy'] == day, 'MxT'].values[0]
        min_t = self.rawdata.loc[self.rawdata['Dy'] == day, 'MnT'].values[0]
        return WeatherDay.WeatherDay(self.year, self.month, day, max_t, min_t)

    def getminexcursionday(self):
        minexcursionday = self.getday('1')  # init
        for day in range(2, self.ndays + 1):
            currentday = self.getday(str(day))
            if currentday.getexcursion() < minexcursionday.getexcursion():
                minexcursionday = currentday

        return minexcursionday
