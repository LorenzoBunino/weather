# weather

_(this is a small exercise)_<br>**Analyze a month\'s worth of weather data, provide insights:** <br>output the day with the smallest thermal excursion
***
* Language: Python
* Standard libraries: datetime, calendar, sys, argparse
* Third party libraries: pandas
* Usage: weather [-h] rawdatafile
* Internal classes: WeatherDay (extends datetime,date), WeatherMonth

A design choice has been made to expect all input as strings, since we are dealing with heterogeneous data that largely comes from text files or console inputs.<br>Data will be properly handled internally.