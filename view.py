# модуль "ОТОБРАЖЕНИЕ" (view)
import text


def show_start_menu() -> int:
    for i, action in enumerate(text.start_menu):
        if i > 0:
            print(f'\t{i} - {action}')
        else:
            print(action)
    while True:
        user_choice = input(text.choice_start_menu)
        if user_choice.isdigit() and 0 < int(user_choice) < len(text.start_menu):
            # сначала проверили цифра ли, а затем смело конвертируем в int
            return int(user_choice)
        else:
            print(text.input_error)


def show_message(msg):
    if msg:
        print('\n' + '=' * len(msg))
        print(msg)
        print('=' * len(msg) + '\n')


def show_dict_phonebook(phone_book: dict, not_found_or_empty=None):
    if phone_book:
        print('\n' + '=' * 64)
        for u_id, contact in phone_book.items():
            print(f'{u_id:>2}. {contact[0]:<18}\t{contact[1]:<15}\t{contact[2]:<25}')
        # :>2 выравнивание по правому краю и выделяем 2 символа, :<18 выравнивание по левому краю и выделяем 18 символов
        print('=' * 64 + '\n')
    else:
        show_message(not_found_or_empty)


def input_data(message) -> list[str] | str:
    if isinstance(message, str):
        return input('\n' + message)
    return [input(msg) for msg in message]


def input_u_id(max_id) -> int:
    while True:
        user_choice = input(text.request_u_id)
        if user_choice.isdigit() and int(user_choice) <= max_id:
            # сначала проверили цифра ли, а затем смело конвертируем в int
            return int(user_choice)
        else:
            print(text.u_id_not_found(user_choice))
