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

# Get Data in Columns
# - Data can be accessed using the column name using square bracket notation or dot notation
print(data["condition"])
print(data.condition)

# Selecting Data in Rows
print(data[data.day == "Monday"])  # Selecting the row where the day is Monday
print(data[data.temp == max_value])  # Selecting the row where the temp is highest

monday = data[data.day == "Monday"]
print(monday.condition)  # Getting a specific column within a row

temp_monday = data[data.day == "Monday"].temp
temp_monday_f = (temp_monday * 9 / 5) + 32
print(temp_monday_f)

### Creating a DataFrame from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
new_data_frame = pandas.DataFrame(data_dict)
print(new_data_frame)
new_data_frame.to_csv("new_data.csv")


# ------------------------------------------------------------------------------------------------ #
#                                            Challenge 1                                           #
# ------------------------------------------------------------------------------------------------ #
squirrel_data = pandas.read_csv("day_25/2018_Squirrel_Data.csv")
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
)
black_squirrels_count = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
)

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

squirrel_data_frame = pandas.DataFrame(squirrel_dict)
print(squirrel_data_frame)
df_squirrel = squirrel_data_frame.to_csv("squirrel")
