# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
#
#
# data=pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict= data.to_dict()
#print(data_dict)


# t=data["temp"].to_list()
# # print(sum(data["temp"])/len(data["temp"]))
# mean=data["temp"].mean()
# #print(mean)
# #print(data["temp"].max())
# #print(data["condition"])
# print(data.condition)
#print(data[data.day == "Monday"])
# print(data[data["temp"] == data["temp"].max()])
# print(data[data.temp == data.temp.max()])
# monday=data[data.day == "Monday"]
# print(monday.condition)
# tem=monday.temp
# tem=(tem*9/5)+32
# print(tem)


import pandas
data_dict = {
    "students":["Any","James","Angela"],
    "scores" : [76,56,65]

}
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



