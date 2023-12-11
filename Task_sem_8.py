def input_data(prompt):
    return input(prompt).title()


def create_contact():
    '''Add an entry'''
    surname = input_data('Введите фамилию: ')
    name = input_data('Введите имя: ')
    patronymic = input_data('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    address = input_data('Введите адрес: ')

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact(file_name):
    contact = create_contact()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read().rstrip().split('\n\n')


def print_contacts(contacts_list):
    for number, contact in enumerate(contacts_list, 1):
        print(f'{number}. {contact}\n')


def copy_contact(source_file, target_file):
    contacts_list = read_file(source_file)
    print_contacts(contacts_list)
    try:
        num_contact = int(input("Введите номер контакта для копирования: ")) - 1
        if num_contact < 0 or num_contact >= len(contacts_list):
            raise IndexError("Нет контакта с таким номером.")
        with open(target_file, 'a', encoding='utf-8') as file:
            file.write(contacts_list[num_contact] + '\n\n')
            print("\nКонтакт скопирован!\n")
    except ValueError:
        print("Введено некорректное число.")
    except IndexError as e:
        print(e)


def search_contact(file_name):
    print(
        "Возможные варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По номеру\n"
        "5. По городу\n"
    )

    try:
        index_var = int(input("Введите вариант поиска: ")) - 1
        search = input("Введите данные для поиска: ").title()

        contacts_list = read_file(file_name)

        found = False
        for contact in contacts_list:
            contact_data = contact.replace('\n', ' ').split(' ')
            if search in contact_data[index_var]:
                print(f'\n{contact}\n')
                found = True
        
        if not found:
            print("Контакт не найден.")

    except ValueError:
        print("Введено некорректное число.")
    except IndexError:
        print("Неверно указан вариант поиска.")


def interface():
    file_name = "phonebook.txt"
    new_file_name = "newphonebook.txt"

    user_input = ""
    while user_input != "5":
        print(
            "Возможные варианты действия:\n"
            "1. Добавить контакт\n"
            "2. Вывод списка контактов\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Выход из программы\n"
        )

        user_input = input("Введите вариант: ")

        if user_input == "1":
            write_contact(file_name)
        elif user_input == "2":
            contacts_list = read_file(file_name)
            print_contacts(contacts_list)
        elif user_input == "3":
            search_contact(file_name)
        elif user_input == "4":
            copy_contact(file_name, new_file_name)


if __name__ == "__main__":
    interface()