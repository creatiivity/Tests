from documents_app.docs_app import DocData


def secretary_program_start(documents, directories):
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы
    """
    print(
        'Вас приветствует программа помошник!\n',
        '(Введите help для просмотра списка поддерживаемых команд)\n'
    )
    user_reaction = True
    while user_reaction:
        current_doc = DocData(documents, directories)
        user_command = input('Введите команду - ')
        if user_command == 'p':
            user_doc_number = input('Введите номер документа - ')
            owner_name = current_doc.get_doc_owner_name(user_doc_number)
            if owner_name:
                print(f'Владелец документа: {owner_name}')
            else:
                print("Такого документа не существует")
        elif user_command == 'ap':
            uniq_users = current_doc.get_all_doc_owners_names()
            print(f'Список владельцев документов: {uniq_users}')
        elif user_command == 'l':
            doc_detailed_info = current_doc.show_all_docs_info()
            print(f'Список всех документов:\n{doc_detailed_info}')
        elif user_command == 's':
            user_doc_number = input('Введите номер документа - ')
            directory_number = current_doc.get_doc_shelf(user_doc_number)
            if directory_number:
                print(f'Документ находится на полке номер {directory_number}')
            else:
                print("Такого документа не существует")
        elif user_command == 'a':
            print('Добавление нового документа:')
            new_doc_n = input('Введите номер добавляемого документа - ')
            new_doc_t = input('Введите тип добавляемого документа - ')
            new_doc_own = input('Введите владельца добавляемого документа - ')
            new_doc_sh = input('Введите полку для размещения добавляемого документа - ')
            doc_already_exists, doc_must_be_shelved = current_doc.add_new_doc(new_doc_n, new_doc_t, new_doc_own, new_doc_sh)
            if not doc_already_exists:
                print(f'Документ {new_doc_t} с номером {new_doc_n} владельца {new_doc_own} добавлен в каталог')
            else:
                print("Такой документ уже существует в каталоге")
            print()
            if doc_must_be_shelved:
                print(f'Документ с номером {new_doc_n} добавлен на полку {new_doc_sh}')
            else:
                print("Такой полки не существует")
            print()
            print(documents)
            print()
            print(directories)
        elif user_command == 'd':
            delete_document = input('Введите номер документа - ')
            removed_from_docs, removed_from_dirs = current_doc.delete_doc(delete_document)
            if removed_from_docs:
                print(f'Документ с номером {delete_document} успешно удален из каталога')
            else:
                print("Такого документа не существует в каталоге")
            if removed_from_dirs:
                print(f'Документ с номером {delete_document} успешно удален из перечня полок')
            else:
                print("Такого документа не существует в перечне полок")
            print()
            print(documents)
            print()
            print(directories)
        elif user_command == 'm':
            move_doc = input('Введите номер документа для перемещения - ')
            move_shelf = input('Введите номер полки для перемещения - ')
            no_such_doc, no_such_shelf = current_doc.move_doc_to_shelf(move_doc, move_shelf)
            if no_such_doc or no_such_shelf:
                print("Такой полки или такого документа не существует")
            else:
                print(f'Документ {move_doc} перемещен на полку {move_shelf}')
                print()
                print(directories)
        elif user_command == 'as':
            new_shelf = input('Введите номер новой полки - ')
            shelf_must_be_added = current_doc.add_new_shelf(new_shelf)
            if shelf_must_be_added:
                print(f'Добавлена полка {new_shelf}')
            else:
                print("Такая полка уже существует")
            print()
            print(directories)
        elif user_command == 'help':
            print(secretary_program_start.__doc__)
        elif user_command == 'q':
            user_reaction = False

