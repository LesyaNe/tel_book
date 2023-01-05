import ui_function as ui_f


def write_file(comment=None):
    id = ui_f.id( )
    name = ui_f.username( )
    surname = ui_f.surname( )
    phone_number = ui_f.phone( )
    comments = ui_f.comments( )

    with open('Phone_Book.csv') as data:
        data.write(f'{id};{name};{surname};{phone_number};{comments}\n')

