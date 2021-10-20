# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит его на экран.
# Дополнительный список не использовать.
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

numbers = [2, 7, 5, 3, 9, 15, 28, -5]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)

