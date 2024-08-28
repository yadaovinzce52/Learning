# import smtplib
#
# my_email = 'pythondevtest52@gmail.com'
# password = 'mbym kufr ussm yuuc'
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='yadaovinzce@gmail.com',
#         msg='Subject:Hello this is a test\n\nThis is the body of the email'
#     )
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1998, month=5, day=4, hour=23)
# print(date_of_birth)

# Monday Motivational Quote
import smtplib
import datetime as dt
from random import choice

my_email = ''
password = ''

with open ('quotes.txt') as file:
    quotes = file.readlines()

day = dt.datetime.now().weekday()
if day == 1:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='',
            msg=f'Subject:Monday Motivation\n\n{choice(quotes)}'
        )
