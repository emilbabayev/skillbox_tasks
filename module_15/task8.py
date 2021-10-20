# Вы пишете программу для маленького табло,
# в котором циклически повторяется один и тот же текст или числа — прямо как в каком-нибудь метро,
# автобусах или трамваях.
# Дан список из N элементов и целое число K.
# Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций.
# Используйте минимально возможное количество операций присваивания.

numbers_count = int(input('Введите кол-во чисел: '))
numbers = []

for i in range(numbers_count):
    num = int(input('Введите число: '))
    numbers.append(num)

shift = int(input('Сдвиг: '))
new_numbers = []

for i in range(numbers_count):
    new_numbers.append(0)

for i in range(len(numbers)):
    new_index = (i + shift) % len(numbers)
    new_numbers[new_index] = numbers[i]

print(numbers)
print(new_numbers)