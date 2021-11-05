# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
# Например, следующие последовательности являются симметричными:

# 1 2 3 4 5 4 3 2 1
#
# 1 2 1 2 2 1 2 1
#
# Пользователь вводит последовательность из N чисел.
# Напишите программу, которая определяет,
# какое минимальное количество и каких чисел надо приписать в конец этой последовательности,
# чтобы она стала симметричной.

num_count = int(input('Кол-во чисел: '))
numbers = list()

for i_number in range(num_count):
    print(i_number + 1, 'число:', end=' ')
    number = int(input())
    numbers.append(number)

print('Последовательность:', numbers)

isSymmetric = True
for i_number in range(num_count):
    if numbers[i_number] != numbers[-(i_number + 1)]:
        print('Последовательность не является симметричной')
        isSymmetric = False
        break
else:
    print('Последовательность является симметричной')


add_count = 0
added_numbers = []
if not isSymmetric:
    for i_number in range(num_count):
        if numbers[i_number] != numbers[-(i_number + 1)] and i_number == 0:
            numbers.append(numbers[i_number])
            add_count += 1
            added_numbers.append(numbers[i_number])
        elif numbers[i_number] != numbers[-(i_number + 1)]:
            numbers.insert(-i_number, numbers[i_number])
            add_count += 1
            added_numbers.append(numbers[i_number])

    added_numbers.reverse()
    print('\nНужно приписать чисел:', add_count)
    print('Сами числа:', added_numbers)
    print('Итоговый список:', numbers)
