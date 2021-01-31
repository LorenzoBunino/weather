# Class containing weather data from a single day


class WeatherDay:
    def __init__(self, day, max_t, min_t):
        self.day = day
        self.max_t = max_t
        self.min_t = min_t

    def getexcursion(self):
        return self.max_t - self.min_t
