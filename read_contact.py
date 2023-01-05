import csv


def read_book():
    with open('Phone_Book.csv') as file:
        csv_f = csv.reader(file)
        data = []
        for row in csv_f:
            data.append(row)
    return data


def read_find(what_find):
    with open('Phone_Book.csv') as file:
        csv_f = csv.reader(file)
        data_find = []
        for row in csv_f:
            for i in row:
                if i == what_find:
                    data_find.append(row)
                else:
                    return None
    return data_find
