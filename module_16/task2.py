# Два класса стоят в две отдельные шеренги. В каждом классе ученики выстроены по росту (по возрастанию):
# в одном классе от 160 см до 176 см с шагом 2, во втором классе — от 162 см до 180 см с шагом 3.
# Спустя какое-то время два класса объединяют в одну шеренгу и тоже выстраивают их по возрастанию.
# Напишите программу, которая генерирует списки роста для каждого в классе,
# затем объединяет их в один список и сортирует его в порядке возрастания.
# Выведите отсортированный список на экран.

class1 = []
class2 = []

for student in range(160, 177, 2):
    class1.append(student)

for student in range(162, 181, 3):
    class2.append(student)

print('Класс 1:', class1)
print('Класс 2:', class2)

class1.extend(class2)
print('Объединены:', class1)

for i_student in range(len(class1)):
    for j_student in range(i_student, len(class1)):
        if class1[i_student] > class1[j_student]:
            class1[i_student], class1[j_student] = class1[j_student], class1[i_student]

print('Отсортированы:', class1)