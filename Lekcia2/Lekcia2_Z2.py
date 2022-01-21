age = int(input('Введите возраст: '))
if 18 <= age <= 27:
    sutd = input('Вы учитесь? (y/n): ').lower()
    if sutd == 'n':
        chld = int(input('Сколько у вас детей?: '))
        if chld < 2:
            height = int(input('Введите рост: '))
            if height < 170:
                print('В танкисты')
            elif height < 185:
                print('На флот')
            elif height < 200:
                print('В десантники')
            else:
                print('В другие войска')
        else:
            print('Вы не можете быть призваны')
    else:
        print('Вам дана отсрочка')
else:
    print('Непризывной возраст')