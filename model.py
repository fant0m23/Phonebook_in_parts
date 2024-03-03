phone_book = {}
path = "file.txt"
SEPAR = ";"


def open_phone_book():
    global phone_book
    with open(path, "r", encoding="utf8") as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):  # 1 - начало нумерации с первого
        phone_book[u_id] = contact.strip().split(SEPAR)
        # по ключу u_id добавляем контакты в словарь-справочник, предварительно удалив служебные символы
        # и конвертировав строки в списки
    return True  # для флага is_open


def save_phone_book():
    global phone_book
    with open(path, "w", encoding="utf8") as file:
        for contact in phone_book.values():
            file.write(SEPAR.join(contact) + '\n')


def _next_id():  # функция с _ в имени означает, что она не будет передаваться в другие модули, только локально!
    global phone_book
    return max(phone_book) + 1 if phone_book else 1


def add_new_contact(new_contact):
    global phone_book
    phone_book[_next_id()] = new_contact


def find_contact(search_word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if search_word.lower() in " ".join(contact).lower():
            result[u_id] = contact
    return result


def edit_contact(u_id, edited_contact: list):
    global phone_book
    current_contact = phone_book[u_id]
    for i in range(len(current_contact)):
        current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
        # т.е. если во входящем параметре edited_contact[i] не None, то записываем его, иначе оставляем без изменений
    phone_book[u_id] = current_contact
    return current_contact[0]  # для передачи в text.edit_contact_successful()


def delete_contact(u_id) -> str:
    global phone_book
    return phone_book.pop(u_id)[0]
    # name = phone_book[u_id][0]
    # del phone_book[u_id]
    # return name


def open_import_phonebook(user_path):
    import_phonebook = {}
    with open(user_path, "r", encoding="utf8") as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):  # 1 - начало нумерации с первого
        import_phonebook[u_id] = contact.strip().split(SEPAR)
        # по ключу u_id добавляем контакты в словарь-справочник, предварительно удалив служебные символы
        # и конвертировав строки в списки
    return import_phonebook


def copy_contact(import_phonebook, u_id) -> str:
    add_new_contact(import_phonebook[u_id])
    return import_phonebook.pop(u_id)[0]
