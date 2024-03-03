start_menu = ['Главное меню',
              'Открыть телефонную книгу',
              'Показать все контакты',
              'Создать новый контакт',
              'Изменить контакт',
              'Удалить контакт',
              'Поиск по контактам',
              'Импортировать контакт',
              'Сохранить изменения',
              'Выход']
choice_start_menu = f"Введите цифру от 1 до {len(start_menu) - 1} >>> "

input_error = "Следует выбирать действие из ПРЕДЛОЖЕННЫХ вариантов !!!"

opened_successful = "Телефонная книга открыта успешно!"
saved_successful = "Телефонная книга сохранена успешно!"
good_bye = 'Спасибо за пользование нашей телефонной книгой!'

empty_phonebook = "Телефонная книга пуста или не была открыта!"

input_new_contact = ['Введите имя контакта: ', 'Введите телефонный номер: ', 'Введите комментарий для контакта: ']

no_changes = '(или нажмите ENTER, чтобы оставить без изменения)'
input_edited_contact = [f'Введите новое имя контакта {no_changes}: ',
                        f'Введите новый телефонный номер {no_changes}: ',
                        f'Введите новый комментарий для контакта {no_changes}: ']

user_search_word = "Введите данные для поиска контакта >>> "
user_search_word_for_edit = "Введите данные для поиска контакта, который хотите изменить >>> "
user_search_word_for_delete = "Введите данные для поиска контакта, который хотите удалить >>> "
request_u_id = "Введите порядковый номер нужного контакта >>> "
request_import_file = "Введите имя файла-справочника, из которого хотите импортировать контакт в формате ****.txt >>> "


def new_contact_added_successful(name):
    return f'Контакт "{name}" успешно добавлен!'


def edit_contact_successful(name):
    return f'Контакт "{name}" успешно изменен!'


def delete_contact_successful(name):
    return f'Контакт "{name}" успешно удален!'


def import_successful(name, where_from='справочника № 2'):
    return f'Контакт "{name}" успешно импортирован из {where_from}!'


def contact_not_found(search_word):
    return f'Контакт содержащий "{search_word}" не найден!'


def u_id_not_found(u_id):
    return f'\nКонтакта c порядковым номером "{u_id}" нет в справочнике!\n'


def phonebook_not_found(name: str):
    return f'Файл-справочник "{name}" не найден!'
