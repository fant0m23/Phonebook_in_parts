import view
import model
import text


def find_contact(message):
    search_word = view.input_data(message)
    dict_with_found_contact = model.find_contact(search_word)
    view.show_dict_phonebook(dict_with_found_contact, text.contact_not_found(search_word))
    return True if dict_with_found_contact else False


def start_app():
    is_open = False
    while True:
        user_choice = view.show_start_menu()
        match user_choice:
            case 1:  # Открыть телефонную книгу
                is_open = model.open_phone_book()
                view.show_message(text.opened_successful)
            case 2:  # Показать все контакты
                view.show_dict_phonebook(model.phone_book, text.empty_phonebook)
                # передаем model.phone_book т.к. она global
            case 3:  # Создать новый контакт
                if is_open:
                    new_contact = view.input_data(text.input_new_contact)
                    model.add_new_contact(new_contact)
                    view.show_message(text.new_contact_added_successful(new_contact[0]))
                else:
                    view.show_message(text.empty_phonebook)
            case 4:  # Изменить контакт
                if is_open:
                    if find_contact(text.user_search_word_for_edit):
                        u_id = view.input_u_id(len(model.phone_book))
                        edited_contact = view.input_data(text.input_edited_contact)
                        name_edited = model.edit_contact(u_id, edited_contact)
                        view.show_message(text.edit_contact_successful(name_edited))
                else:
                    view.show_message(text.empty_phonebook)
            case 5:  # Удалить контакт
                if is_open:
                    if find_contact(text.user_search_word_for_delete):
                        u_id = view.input_u_id(len(model.phone_book))
                        name_deleted = model.delete_contact(u_id)
                        view.show_message(text.delete_contact_successful(name_deleted))
                else:
                    view.show_message(text.empty_phonebook)
            case 6:  # Поиск по контактам
                find_contact(text.user_search_word) if is_open else view.show_message(text.empty_phonebook)
            case 7:  # Импортировать контакт
                if is_open:
                    import_file_name = view.input_data(text.request_import_file)
                    try:
                        import_phonebook = model.open_import_phonebook(import_file_name)
                        view.show_dict_phonebook(import_phonebook, text.empty_phonebook)
                        u_id = view.input_u_id(len(import_phonebook))
                        name_imported = model.copy_contact(import_phonebook, u_id)
                        view.show_message(text.import_successful(name_imported, import_file_name))
                    except FileNotFoundError:
                        view.show_message(text.phonebook_not_found(import_file_name))
                else:
                    view.show_message(text.empty_phonebook)
            case 8:  # Сохранить изменения
                if is_open:
                    # без этой проверки "затрёт" исходный file.txt при выборе "Сохранить" ранее чем "Открыть тел. книгу"
                    model.save_phone_book()
                    view.show_message(text.saved_successful)
                else:
                    view.show_message(text.empty_phonebook)
            case 9:  # Выход
                view.show_message(text.good_bye)
                break
