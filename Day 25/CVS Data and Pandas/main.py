# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#     for temp in temperatures:
#         print(temp)
#

import pandas

data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(type(data['condition']))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temps = data['temp'].to_list()
#
# print(data['temp'].mean())
#
# print(data['temp'].max())
#
# # Get Data in Columns
# # The lines below are the exact same
# # just different methods of getting the columns
# # Case sensitive
# print(data['condition'])
# print(data.condition)

# Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
# # (0°C × 9/5) + 32 = 32°F
# print((monday.temp * 9/5) + 32)

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
