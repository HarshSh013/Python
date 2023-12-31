# import smtplib
# my_email="sharmaeater1@gmail.com"
# password="eljznatvitfzlniv"
# connection=smtplib.SMTP("smtp.gmail.com",587)
# #for security purpose
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="sharmaeater2@gmail.com",msg="Subject:Hello\n\nThis is the body")
# connection.close()
#
# # import datetime as dt
# #
# # now = dt.datetime.now()
# # year=now.year
# # month=now.month
# # day_of_week=now.weekday()
# # print(year,month,day_of_week)
# # date_of_birth=dt.datetime(year=2002,month=6,day=13,hour=17,minute=5)
# # print(date_of_birth)
# import smtplib
# import random
# import datetime as dt
#
#
# my_email="sharmaeater1@gmail.com"
# password="eljznatvitfzlniv"
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#         connection.starttls()
#         connection.login(my_email, password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="sharmaeater2@gmail.com",
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )
#
from datetime import datetime
time_now = datetime.now()
hour=time_now.hour
print(type(hour),hour)
