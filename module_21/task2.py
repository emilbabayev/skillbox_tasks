# Написав аналог функции zip на собеседовании, вы вспомнили, что этот код можно сделать даже лучше,
# и резко вырвали листок с кодом из рук работодателя, оставив его в недоумении.
#
# Напишите функцию, которая будет являться аналогом функции zip и сделайте так,
# чтобы программа работала с любыми итерируемыми типами данных.
# Циклами за исключением генераторов, условными операторами и функциями определения типа (isinstance или type)
# пользоваться нельзя.
# Функция должна возвращать список из пар кортежей.

def my_zip(iterable1, iterable2):
    zip_tuple = ((el1, el2)
                 for i_el1, el1 in enumerate(iterable1)
                 for i_el2, el2 in enumerate(iterable2)
                 if i_el1 == i_el2)

    return zip_tuple


numbers = '0123456789'
people = ['Emil', 'Alex', 'Samir', 'Sabina', 'Liana', 'Ksenia']

for element in my_zip(numbers, people):
    print(element)