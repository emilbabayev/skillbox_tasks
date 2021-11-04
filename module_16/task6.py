# Даны два списка целых чисел, оба списка заполняются с клавиатуры.
# В первый список вводится три числа, во второй — семь чисел.
# Напишите программу, которая запрашивает у пользователя эти числа,
# затем расширяет первый список элементами второго и после этого оставляет в первом списке
# только уникальные элементы, то есть удаляет лишние повторы чисел.
# Условный оператор использовать нельзя.


list1 = []
list2 = []

print('СПИСОК 1')
for i_num in range(3):
    number = int(input(f'Введите {i_num + 1} число: '))
    list1.append(number)

print()
print('СПИСОК 2')
for i_num in range(7):
    number = int(input(f'Введите {i_num + 1} число: '))
    list2.append(number)

print('Первый список: ', list1)
print('Второй список: ', list2)

list1.extend(list2)

temp = 0
for i_num in range(len(list1)):
    if list1.count(list1[i_num - temp]) > 1:
        list1.remove(list1[i_num - temp])
        temp += 1

# Есть баг

# for element in list1:
#     count = list1.count(element)
#     for index in range(count - 1):
#         list1.remove(element)


print('Объединенный список с уникальными элементами:', list1)