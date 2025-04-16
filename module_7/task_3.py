student_count = int(input('Сколько в классе учеников? '))
count_3, count_4, count_5 = 0, 0, 0


for student in range(student_count):
    grade = int(input('Введите оценку ученика: '))
    if grade == 3:
        count_3 += 1
    elif grade == 4:
        count_4 += 1
    elif grade == 5:
        count_5 += 1


if count_3 > count_4 and count_3 > count_5:
    print('Сегодня больше троечников!')
elif count_4 > count_3 and count_4 > count_5:
    print('Сегодня больше хорошистов!')
elif count_5 > count_3 and count_5 > count_4:
    print('Сегодня больше отличников!')
else:
    print('Каких-то из оценок одинаковое кол-во')