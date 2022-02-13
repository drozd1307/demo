# d + delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
#       Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
#       Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
#       Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

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


# def del_doc(docs, dris):
#     doc_num = input('Введите номер документа: ')
#     def del_dirs(dirs):
#         for k, val in dirs.items():
#             if doc_num in val:
#                 val.remove(doc_num)
#                 print(val)
#                 print(dirs)
#     # doc_num = input('Введите номер документа: ')
#     rec = 0
#     for record in docs:
#         if doc_num in record.values():
#             docs.pop(rec)
#             print('Документ успешно удален')
#             del_dirs(dris)
#             return
#         rec += 1
#     else:
#         print('Такого документа не существует')
# del_doc(documents, directories)

# def move_dir(dirs):
#     doc_num = input('Введите номер документа: ')
#     tag_dir = input('На какую полку поместить: ')
#     for k, val in dirs.items():
#         if doc_num in val:
#             val.remove(doc_num)
#             if tag_dir in dirs.keys():
#                 dirs[tag_dir].append(doc_num)
#             else:
#                 print('Такой полки не существует.')
#             return
#     else:
#         print('Такого документа не существует.')

def add_shelf(dirs):
    tag_dir = input('Введите номер, новой полки: ')
    if tag_dir in dirs.keys():
        print('Такая полка уже есть.')
    else:
        dirs[tag_dir] = []
        print(dirs)
add_shelf(directories)