def make_operation(data):
    operand_1, operator, operand_2 = data[0], data[1], data[2]
    if len(data) != 3:
        raise IndexError

    if operator not in ('+', '-', '*', '/', '//', '%', '**'):
        raise KeyError

    operand_1 = int(operand_1)
    operand_2 = int(operand_2)

    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2
    elif operator == '//':
        return operand_1 // operand_2
    elif operator == '%':
        return operand_1 % operand_2
    elif operator == '**':
        return operand_1 ** operand_2


summary = 0

with open('calc.txt', 'r') as calc_file:
    for i, line in enumerate(calc_file):
        try:
            user_data = line.split()
            summary += make_operation(user_data)

        except ZeroDivisionError:
            print(f'Строка {i + 1}: Обнаружено деление на ноль')
        except IndexError:
            print(f'Строка {i + 1}: Неверный формат данных')
        except KeyError:
            print(f'Строка {i + 1}: Неизвестный оператор')
        except ValueError:
            print(f'Строка {i + 1}: Ошибка. Операнды могут быть только целыми числами')

print(f'\nСумма результатов проведенных операций: {summary}')