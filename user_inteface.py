import save_contact as save_cont
import read_contact as read_cont
import writing as wr


def do_it() -> object:
    question = input(f'Выберите действие: добавить контакт - нажмите 1, найти контакт - нажмите 2, посмотреть всю книгу - нажмите 3, импортировать тел.книгу -нажмите 4 ')
    if question == "1":
        save_cont.write_file( )
    elif question == "2":
        for i in read_cont.read_find(input('Введите информацию контакта, которого необходимо найти: ')):
            print (i)
    elif question == "3":
        for i in read_cont.read_book( ):
            print(i)
    elif question == "4":
        a = input(f'Выберите как импортировать: в scv - нажмите 1, в текст - нажмите 2')
        if a == "1":
            wr.writing_scv( )
        elif a == "2":
            wr.writing_txt( )

    else:
        print('Введено не корректное число')
        return do_it( )
