# Class containing weather data from a single day

import datetime


class IllegalWeatherDay(Exception):
    pass


class WeatherDay(datetime.date):
    def __new__(cls, year, month, day: str, max_t, min_t):  # overridden because datetime.date is immutable
        day = int(day)
        self = super().__new__(cls, year, month, day)  # raises ValueError on illegal date; wrap in IllegalWeatherDay?
        self.max_t = WeatherDay.__atoi(max_t)
        self.min_t = WeatherDay.__atoi(min_t)
        self.__validatemaxmin(self.max_t, self.min_t)
        return self

    @staticmethod
    def __atoi(literal):  # "special" type caster
        try:
            return int(literal)
        except ValueError:
            return int(WeatherDay.__stripastherisc(literal))

    @staticmethod
    def __validatemaxmin(max_t, min_t):
        if max_t < min_t:
            raise IllegalWeatherDay('Max temperature ' + str(max_t) + ' is lower than min temp ' + str(min_t))

    @staticmethod
    def __stripastherisc(literal):  # "*" indicates month absolute max/min, unused data in this program as of now
        return literal.replace('*', '')

    def getexcursion(self):
        return self.max_t - self.min_t

    def __str__(self):
        return super().__str__() + ', %d°F excursion' % self.getexcursion()
