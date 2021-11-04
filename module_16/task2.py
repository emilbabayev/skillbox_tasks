class1 = []
class2 = []

for student in range(160, 176, 2):
    class1.append(student)

for student in range(162, 180, 3):
    class2.append(student)

print('Класс 1:', class1)
print('Класс 2:', class2)

class1.extend(class2)
print('Обьединены:', class1)

for i_student in range(len(class1)):
    for j_student in range(i_student, len(class1)):
        if class1[i_student] > class1[j_student]:
            class1[i_student], class1[j_student] = class1[j_student], class1[i_student]

print('Отсортированы:', class1)