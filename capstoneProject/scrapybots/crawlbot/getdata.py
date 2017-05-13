# Python file to read in the csv data

import pandas as pd


pd.options.display.max_rows = 400
pd.options.display.max_columns = 100
data = pd.read_csv('./capstone_data.csv')

print(data.head())
print(data.shape)


#
# # print(data.Route.value_counts())
# # print(data.Date.value_counts())
#
#
#
# # Split the Date into Year Month and Day
#
# from datetime import datetime as dt
#
# print(data.Date.dtypes)
# print(data.columns)
# data['Year'] = pd.DatetimeIndex(data['Date']).year
# data['Month'] = pd.DatetimeIndex(data['Date']).month
# data['Day'] = pd.DatetimeIndex(data['Date']).day
# data['Time'] = pd.DatetimeIndex(data['Date']).time
#
# print(data.columns)
# print(data.head())
#
# # unknown_route = ((data[data['Route'] == '?']))
# # unknown_years = pd.DataFrame(unknown_route.Year.value_counts())
# # print(unknown_years.sort_index())
#
# # unknown_location = ((data[data['Location'] == '?']))
# # unknown_loc = pd.DataFrame(unknown_location.Location.value_counts())
# # print(unknown_location.Location.value_counts())
#
#
# print((data[data['Year'] == 2017]))