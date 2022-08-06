##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import pandas
import datetime as dt
from random import choice

LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = "pythonburner56@gmail.com"
MY_PASS = "jnkdxbyquemkzeqn"
today_date = dt.datetime.today()
current_month = today_date.month
day_of_month = today_date.day
print(current_month, day_of_month)


def send_email(letter):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="tristinen38@gmail.com",
                            msg=f"Subject:Phillip's Automated Test\n\n {letter}")




# list comprehension to find the persons' birthday in the dictionary that matches the value
def getKey(dct, value):
    return [key for key in dct if (dct[key] == value)]


# converts random letter to string and replaces name spot with the person whose birthday it is
def convert_letter_to_str(letter, bday_dict, value):
    print(letter)
    print(bday_dict)
    print(value)
    friends_bday = getKey(bday_dict, value)
    f_bday_str = "".join(friends_bday)
    with open(letter, "r") as letter_file:
        bday_letter = letter_file.readlines()
        bday_list_to_str = " ".join([str(elem) for elem in bday_letter])
        x = bday_list_to_str.replace("[NAME]", f_bday_str)
        send_email(x)

# pull information from pandas dataframe
def search_bday_file():
    dictionary = {}
    dataa = pandas.read_csv("birthdays.csv")
    for i in range(len(dataa)):
        name = dataa.loc[i, "name"]
        month = dataa.loc[i, "month"]
        day = dataa.loc[i, "day"]
        print(name, month, day)
        dictionary[name] = month, day
    return dictionary


random_letter = choice(LETTERS)
print(random_letter)
bday_dict = search_bday_file()
for dates in bday_dict.values():
    print(dates)
    if current_month == dates[0] and day_of_month == dates[1]:
        value = dates
        convert_letter_to_str(random_letter, bday_dict, value)
    else:
        print("It is no ones birthday")