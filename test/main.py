import csv
import pandas as pd
# # Take the temperature from the file in a list
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     # Make a list from data = object of csv.reader
#     for item in list(data)[1:]:  # from the second row not the "temp"
#         temperature.append(int(item[1]))
# print(temperature)


# Using a library call as PANDA
data = pd.read_csv("weather_data.csv")
# # Type of data is a DataFrame = a sheet(table) of an excel file
# print(type(data))
# # Types of data is a Series = Στηλη στο excel
# print(type(data.temp))
# varo = data.to_dict()
# print(varo)

# lists = data.temp.to_list()
# print(lists)
#
# summary = data["temp"].sum()
# print(summary)
# average = summary / data.temp.size
# # # Equal with the above code
# # average= sum / data["temp"].size
#
# print(average)
#
# # Using the PANDA
# pd_average = data.temp.mean()
# print(pd_average)
#
# pd_maximum_value = data["temp"].max()
# print(pd_maximum_value)
# # Equal with
# pd_maximum_value_alternative = data.temp.max()
# print(pd_maximum_value_alternative)
#
#
# # Get data from ROW
# print(data[data.day == "Monday"])

# # Find the day of the week with the max temp
# max_temp = data.temp.max()
# # print(max_temp)
#
# print(data[data.temp == max_temp])

# Transform temp to Fahrenheit using the Formula
# (0°C × 9/5) + 32 = 32°F
monday = data[data.day == "Monday"]
fahrenheit = (int(monday.temp) * 9/5)+32
print(f"{fahrenheit}F")

# Create Dataframe from Scratch using a given dictionary

data_dict = {
    "student": ["amy","Jenna", "Angela"],
    "scores": [79,55,26]
}
data = pd.DataFrame(data_dict)
print(data)
# Save to a csv
data.to_csv("export_to.csv",columns=None)

