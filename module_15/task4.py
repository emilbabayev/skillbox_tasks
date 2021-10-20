# В базе одного магазина электроники есть список видеокарт компании NVIDIA разных поколений.
# Для удобства в списке вместо полных названий хранятся только числа, они обозначают модель и поколение видеокарты.
# Недавно компания выпустила новую линейку видеокарт, и в итоге самые старшие поколения разобрали за пару дней.

# Напишите программу, которая удаляет из этого списка видеокарт наибольшие элементы.

vga_count = int(input('Введите кол-во видеокарт: '))
vga = []

for i in range(vga_count):
    print(i + 1, 'видеокарта:', end=' ')
    vga_model = int(input())
    vga.append(vga_model)

maximum = vga[0]
maximum_id = 0

for i in range(vga_count):
    if vga[i] > maximum:
        maximum = vga[i]
        maximum_id = i

new_vga = []

for i in range(vga_count):
    if vga[i] != vga[maximum_id]:
        new_vga.append(vga[i])

print(vga)
print(new_vga)


