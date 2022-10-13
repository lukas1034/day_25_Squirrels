import pandas

# mine
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# squirrel_colour = data["Primary Fur Color"].value_counts()
# print(squirrel_colour)
# new_data = pandas.DataFrame(data=squirrel_colour, columns=['Fur Color', 'Count'])
# print(new_data)
# new_data.to_csv("new_data.csv")
# key
data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")