# Пользователь вводит строку. Необходимо написать программу,
# которая определяет, существует ли у этой строки такая перестановка, при которой она станет палиндромом.
# Выведите соответствующее сообщение.

text = input('Введите строку: ')

letters_dict = dict()

for sym in text:
    letters_dict[sym] = letters_dict.get(sym, 0) + 1

counts = list(letters_dict.values())

odd_numbers = 0
for num in counts:
    if num % 2 != 0:
        odd_numbers += 1
    if odd_numbers > 1:
        print('Нельзя сделать палиндромом')
        break
else:
    print('Можно сделать палиндромом')
