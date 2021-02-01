# User-facing CLI

import sys
import argparse

import WeatherMonth


def main():
    rawdatafile_help = 'a file containing month\'s weather data'

    parser = argparse.ArgumentParser(description='Analyze a month\'s worth of weather data, provide insights')
    parser.add_argument('rawdatafile', help=rawdatafile_help)

    namespace = parser.parse_args()

    month = WeatherMonth.WeatherMonth(namespace.rawdatafile, 2020, 6)  # assuming June 2020 since it's unspecified
    print('- A month\'s weather data -\n')
    print(month.getminexcursionday())


if __name__ == '__main__':
    sys.exit(main())
