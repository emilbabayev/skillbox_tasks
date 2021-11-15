# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждому элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам нужно написать программу, которая по заданному генеалогическому древу определяет высоту всех его элементов.
#
# Программа получает на вход N количество человек в генеалогическом древе.
# Далее следует N−1 строк, в каждой из которых задаётся родитель для каждого элемента дерева,
# кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту).
# После вывода имени каждого элемента необходимо вывести его высоту.

people_count = int(input('Введите кол-во людей в дереве: '))
family_tree = dict()
all_people = set()

for i_people in range(people_count - 1):
    couple = input('{} пара: '.format(i_people + 1)).split()
    child = couple[0].lower()
    parent = couple[1].lower()
    all_people.add(child)
    all_people.add(parent)

    if family_tree.get(parent):
        family_tree[parent].append(child)
    else:
        family_tree[parent] = list()
        family_tree[parent].append(child)


all_children = {child for children in family_tree.values() for child in children}
all_parents = {parent for parent in family_tree.keys()}

ancestor = all_parents - all_children
for el in ancestor:
    ancestor = el

levels = {ancestor: 0}

for parent in family_tree.keys():
    for child in family_tree[parent]:
        if parent in levels.keys():
            levels[child] = levels[parent] + 1

print()
print('Высота каждого члена семьи:')
for name in levels.keys():
    print('{name} - {level}'.format(
        name=name.capitalize(),
        level=levels[name]
    ))
