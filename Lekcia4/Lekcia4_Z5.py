# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

my_list = ['2018-01-01', 'yandex', 'cpc', 100]

my_list.reverse()
my_dict = {}
new_dict = {}
my_dict[my_list[1]] = my_list[0]
for num in my_list[2:]:
    new_dict[num] = my_dict
    my_dict = new_dict.copy()
    new_dict.clear()
print(my_dict)




