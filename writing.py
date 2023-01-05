from user_inteface import do_it as di

info = di()
def writing_scv():
    file = 'Phone_book.csv'
    with open(file) as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt() -> object:
    file = 'Phone_book.txt'
    with open(file) as data:
        data.write(f'surname: {info[0]}\n\nusername: {info[1]}\n\nphone_num: {info[2]}\n\ncomments: {info[3]}\n\n\n')

