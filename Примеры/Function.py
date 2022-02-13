def square(number):
    '''
    this is my first function
    '''
    result = number ** 2
    return result


num = 547
# print()

res = square(num)


# print(res)

# help(square)

def square_2():
    user_input = int(input('Введите число'))
    result = user_input ** 2
    return result


# print(square_2())

def power(number, number_2=2, number_3=7):
    result = number ** number_2 / number_3
    return result


# print(power(2, 45))

# a = (1, 2, 3)
# b = a

# b.append(4)

# print(a)

#


salary = 1000
bonus = 600


def info():
    print(salary + bonus)


def info_2():
    bonus = 50
    print(salary + bonus)


def local_info():
    salary = 500
    bonus = 200
    some_number = 1
    print(salary + bonus)


# info_2()
# local_info()
# info()

# print(salary)
# print(some_number)

# def local_info():
#     # global salary
#     salary = 500
#     bonus = 200
#     some_number = 1
#     print(salary + bonus)

# print(salary)
# local_info()
# print(salary)

# func = lambda x, y: x + y


# print(func(1, 5))


# map(, )

# def some_func(*args):
#   print(args)
#   for arg in args:
#     print(arg / 2)

# some_func(1, 2, 3)
# some_func(1)
# some_func(1, 54, 65, 7, 8, 86, 86)

students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м", "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "program_exp": False, "grade": [10, 9, 8, 10, 10],
     "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "program_exp": False, "grade": [7, 8, 8, 9, 8],
     "exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 5},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6}
]


def get_avg_hw_grade(students, exp=None, gender=None):
    sum_grade = 0
    counter = 0
    for student in students:
        if (student['program_exp'] == exp or exp is None) and \
                (student['gender'] == gender or gender is None):
            sum_grade += sum(student["grade"]) / len(student["grade"])
            counter += 1
    return round(sum_grade / counter, 2)


# print(get_avg_hw_grade(students_list))
# print(get_avg_hw_grade(students_list, True))
# print(get_avg_hw_grade(students_list, False))
# print(get_avg_hw_grade(students_list, False, 'м'))
# print(get_avg_hw_grade(students_list, False, 'ж'))

# print(get_avg_hw_grade(students_list, None, 'ж'))
# print(get_avg_hw_grade(students_list, gender='ж'))

def main(students):
    while True:
        comand = input('Введите команду')
        if comand == '1':
            print(get_avg_hw_grade(students))
        elif comand == '2':
            print(get_avg_hw_grade(students, True))
        elif comand == '3':
            print(get_avg_hw_grade(students, None, 'ж'))
        elif comand == 'q':
            print('Выход из программы')
            break


main(students_list)