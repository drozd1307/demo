# x = input("Введите первое число: ")
# y = input("Введите второе число: ")
# print("x + y =", int(x) + int (y))

lost = ['what is going on']
lost_1 = ['1 2 3 4']
lost = lost[0].split(' ')
lost_1 = lost_1[0].split(' ')
power_lost = []

for lost, lost_1 in zip(lost, lost_1):
    lost = [lost, ]
    lost_1 = [lost_1, ]
    power_lost += [*lost, *lost_1]
print(power_lost)