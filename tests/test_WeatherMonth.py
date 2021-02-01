from unittest import TestCase
import io

import weather


class TestWeatherMonth(TestCase):
    real_f = r'C:\weather.dat'

    def test_getminexcursionday_normal(self):
        self.assertEqual(
            weather.WeatherMonth.WeatherMonth(TestWeatherMonth.real_f, '2020', '6').getminexcursionday().getexcursion(),
            2
        )

    def test_getday_empty_garbage(self):
        f = io.StringIO('abc\nde')
        with self.assertRaises(weather.WeatherMonth.IllegalWeatherMonth) as context:
            weather.WeatherMonth.WeatherMonth(f, '2018', '8').getday('1')

    def test_getday_wrong_day_type(self):
        with self.assertRaises(TypeError) as context:
            weather.WeatherMonth.WeatherMonth(TestWeatherMonth.real_f, 2020, 8).getday([20])

    def test_getday_wrong_day_value(self):
        with self.assertRaises(ValueError) as context:
            weather.WeatherMonth.WeatherMonth(TestWeatherMonth.real_f, 2020, 8).getday('45')

    # ! Uncovered a bug / inconsistency
    # def test_getday_wrong_day_value(self):
    #     f = r'C:\Users\Giorgio\Desktop\Companies\ISCS\Programming Tests\Weather\data\weather.dat'
    #     with self.assertRaises(ValueError) as context:
    #         weather.WeatherMonth.WeatherMonth(f, 2020, 8).getday('45')

