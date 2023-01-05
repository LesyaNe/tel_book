import csv


def id():
    with open ('PhoneBook.csv') as file:
        reader = csv.reader (file)
        data = list (reader)
        id = len (data) + 1
        return id


id ( )


def username():
    username = input ('Напишите имя: ')
    return username


def surname():
    surname = input ('Напишите фамилию: ')
    return surname


def phone():
    phone_num = input ('Напишите номер телефона: ')
    return phone_num


def comments():
    comments = input ('Напишите комментарий: ')
    return comments
