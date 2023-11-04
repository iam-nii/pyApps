# with open("weather_data.csv") as data_file:
#     data = (data_file.read()).splitlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dictionary = data.to_dict()
# print(data_dictionary)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# Old way of calculating the mean
# total_temperature = 0
# for temp in temp_list:
#     total_temperature += int(temp)
#
# average_temperature = total_temperature / len(temp_list)
# print(average_temperature)

# New way
# average = data["temp"].mean()
# print(average)
#
# maximum = data["temp"].max()
# print(maximum)
#
# # Get Data in columns
# print(data["condition"])
# print(data.condition)


# Printing a specific row of data
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# challenge: get mondays temperature in kelvin
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# fahrenheit = int(monday_temp) * 9/5 + 32
# print(f"Monday's temperature in fahrenheit was {fahrenheit}f")


# Creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "Seth", "Jeffrey", "Victoria"],
    "scores": [80, 48, 90, 10]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
