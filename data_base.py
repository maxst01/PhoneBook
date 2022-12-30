import phone_book as pb
path = r'phone_book.txt'

def load_contacts() -> list:
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readline()
        pb.set_phone_book(str_to_list(data))
    print('Телефонная книга загружена \n')


def save_contacts(phone_book: str):
    global path
    ready_book = list_to_str(pb.get_phone_book())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)
    print('Телефонная книга сохранена\n')
   


def list_to_str(phone_book: list) -> str:
    str_phone_book =''
    for contact in phone_book:
        new_contact = ';'.join(contact)
        str_phone_book += new_contact + '\n'
    return str_phone_book[:-1]

def str_to_list(phone_book: list) -> list:
    new_list = []
    for contact in phone_book:
        new_contact = contact.strip().splist(';')
        new_list.append(new_contact)
    return new_list
        



