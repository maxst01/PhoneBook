import phone_book as pb

def main_menu():
    print ('Выберите команду меню')
    print ('1.Показать телефонную книгу')
    print ('2.Загрузить телефонную книгу')
    print ('3.Сохранить телефонную книгу')
    print ('4.Добавить контакт')
    print ('5.Изменить контакт')
    print ('6.Удалить контакт')
    print ('7.Найти контакт')
    print ('0.Выйти из приложения')
    return input_menu()


    def input_menu():
        while True:
            choice = int(input('Введите пункт меню'))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('Такого пункта меню нет')


def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('телефонная книга пуста или не загружена\n')
    else:
        for id, contact in enumerate(phone_book, 1 ):
            print(id, *contact)
    print()


def input_new_contact():
    name = input('Введите имя контакта')
    phone = input('Введите телефон контакта')
    comment = input('Введите коментарий')
    new_contact = [name, pgone, comment]
    return new_contact


def import_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID контакта, который стоит удалить'))
    return id
        