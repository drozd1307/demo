boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()
if len(boys) == len(girls):
    print (f"Идеальные пары:")
    for merg in zip(boys, girls):
        print(merg[0], 'и', merg[1])
else:
  print("Кто-то может остаться без пары!")