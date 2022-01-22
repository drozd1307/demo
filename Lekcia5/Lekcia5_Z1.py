# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# + p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# + s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# + Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# + l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
#       имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда
#       пользователь будет пытаться добавить документ на несуществующую полку.
#
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций.
# Функции должны иметь выразительное название, передающие её действие.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def find_item(docs):
    num = input('Введите номер документа: ')
    for record in docs:
        if num in record["number"]:
            print(f'Документ принадлежит: {record["name"]}')
            return
    else:
        print('Указанного документа не существует.')


def find_dir(dirs):
    num = input('Введите номер документа: ')
    for k, val in dirs.items():
        if num in val:
            print(f'Документ с номером {num}, находится на полке {k}')
            return
    else:
        print('Указанного документа не существует.')


def all_rec(all_doc):
    for record in all_doc:
        print(f'Документ: {record["type"]} "{record["number"]}" "{record["name"]}"')
    return


def add_record(docs, dirs):
    doc_type = input('Введите тип документа: ')
    doc_num = input('Введите номер документа: ')
    name_doc = input('Введите имя владельца: ')
    num_dir = input('Введите номер полки: ')
    docs.append({"type": doc_type, "number": doc_num, "name": name_doc})
    for k in dirs.keys():
        if num_dir == k:
            dirs[num_dir].append(doc_num)
            print(f'Документ {doc_type} {doc_num} {name_doc}, успешно добавлен на полку {num_dir}')
            return
    else:
        print('Такой полки не сущестует')


def del_doc(docs, dris):
    doc_num = input('Введите номер документа: ')
    def del_dirs(dirs):
        for k, val in dirs.items():
            if doc_num in val:
                val.remove(doc_num)
    rec = 0
    for record in docs:
        if doc_num in record.values():
            docs.pop(rec)
            print('Документ успешно удален')
            del_dirs(dris)
            return
        rec += 1
    else:
        print('Такого документа не существует')


def move_dir(dirs):
    doc_num = input('Введите номер документа: ')
    for k, val in dirs.items():
        if doc_num in val:
            tag_dir = input('На какую полку поместить: ')
            val.remove(doc_num)
            if tag_dir in dirs.keys():
                dirs[tag_dir].append(doc_num)
            else:
                print('Такой полки не существует.')
            print('Документ успешно перемещен.')
            return
    else:
        print('Такого документа не существует.')


def add_shelf(dirs):
    tag_dir = input('Введите номер, новой полки: ')
    if tag_dir in dirs.keys():
        print('Такая полка уже есть.')
    else:
        dirs[tag_dir] = []
        print('Полка успешно добалена.')

def menu ():
    while True:
        com = input('Введите команду: ').lower()
        if com == 'p':
            find_item(documents)
        elif com == 's':
            find_dir(directories)
        elif com == 'l':
            all_rec(documents)
        elif com == 'a':
            add_record(documents, directories)
        elif com == 'd':
            del_doc(documents, directories)
        elif com == 'm':
            move_dir(directories)
        elif com == 'as':
            add_shelf(directories)
        elif com == 'q':
            break
        else:
            print('Такой команда не существует')


menu()