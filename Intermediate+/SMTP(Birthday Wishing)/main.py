##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

#
# now = dt.datetime.now()
# tmonth=now.month
# tday=now.day
#
# df=pandas.read_csv("birthdays.csv")
#
# # Initialize an empty dictionary to store the birthdays
# birthdays_dict = {}
#
# # Iterate through the DataFrame rows and populate the dictionary
# for index, row in df.iterrows():
#     name = row['name']
#     email = row['email']
#     month = row['month']
#     day = row['day']
#     birthdays_dict[(month, day)] = {'name': name, 'email': email}
#
# # Print the resulting dictionary
# # print(birthdays_dict)
#
# if (tmonth,tday) in birthdays_dict:
#     with open(f"letter_templates/letter_{random.randint(1,3)}.txt","r") as quote_file:
#         all_lines = quote_file.read()
#     birthday_person = birthdays_dict[(tmonth, tday)]
#     name = birthday_person['name']
#     modified_lines = [line.replace('[NAME]', name) for line in all_lines]
#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#         connection.starttls()
#         connection.login(my_email, password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=birthday_person['email'],
#             msg=f"Subject:Happy Birthday!\n\n{modified_lines}"
#         )
# # if weekday == 1:
# #     with open("quotes.txt") as quote_file:
# #         all_quotes = quote_file.readlines()
# #         quote = all_quotes[1]
# #
# #     print(quote)
# #
# #     with smtplib.SMTP("smtp.gmail.com",587) as connection:
# #         connection.starttls()
# #         connection.login(my_email, password)
# #         connection.sendmail(
# #             from_addr=my_email,
# #             to_addrs="sharmaeater2@gmail.com",
# #             msg=f"Subject:Monday Motivation\n\n{quote}"
# #         )





import smtplib
import datetime as dt
import pandas
import random

my_email="sharmaeater1@gmail.com"
password="eljznatvitfzlniv"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


