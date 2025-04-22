text = input('Что написано в свитке? ')
reversed_text = ''

for sym in text:
    reversed_text = sym + reversed_text

if text == reversed_text:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром')