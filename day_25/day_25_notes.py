# ------------------------------------------------------------------------------------------------ #
#                            Working with CSV Data & the Pandas Library                            #
# ------------------------------------------------------------------------------------------------ #

### Reading CSV Data in Python
import csv

with open("day_25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)


### Reading CSV with Pandas
import pandas

data = pandas.read_csv("day_25/weather_data.csv")
print(data)
print(data["temp"])

# - Pandas has two data structures
# - 1) Series -> a column (similar to a list / single column in an excel sheet)
# - 2) DataFrame -> the equivalent of an entire sheet in an excel sheet
# - Several series will make up a DataFrame

print(type(data))  # A DataFrame (entire excel sheet)
print(type(data["temp"]))  # A series (a row)

### Converting a DataFrame
data_dict = data.to_dict()  # converting a DataFrame to a dictionary
print(data_dict)

### Converting a Series
temp_list = data["temp"].to_list()  # converting the temp series to a list
print(temp_list)


### Working with Pandas
#! Find average the old way
average = sum(temp_list) / len(temp_list)
print(average)

# Finding average with Pandas
average2 = data["temp"].mean()  # Finding average using Pandas
print(average2)

# Finding the max value with Pandas
max_value = data["temp"].max()
print(max_value)

# Selecting Columns
# - Data can be accessed using the column name using square bracket notation or dot notation
print(data["condition"])
print(data.condition)
