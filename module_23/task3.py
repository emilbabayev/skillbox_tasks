import random

summary = 0
exceptions_list = (BaseException, ZeroDivisionError, TypeError, ValueError, FileNotFoundError,
                   IndexError, FloatingPointError, RuntimeError, SyntaxError, EOFError, OSError,
                   AssertionError, ConnectionAbortedError, KeyboardInterrupt, RecursionError,
                   UnicodeError, TimeoutError, NameError, ModuleNotFoundError, ChildProcessError)

with open('nums_file.txt', 'a') as nums_file:
    while summary < 777:
        if random.randint(1, 13) == 1:
            raise random.choice(exceptions_list)

        user_num = int(input('Введите число: '))
        summary += user_num

        nums_file.write(f'{user_num}\n')

print('Ввод окончен. Сумма больше 777')