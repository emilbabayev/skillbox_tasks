errors_data = ''

with open('people.txt', 'r') as file:
    for i, i_line in enumerate(file):
        line_length = 0
        if i_line.endswith('\n'):
            line_length = len(i_line) - 1
        else:
            line_length = len(i_line)

        try:
            if line_length < 3:
                errors_data += i_line
                raise ValueError()
        except ValueError:
            print(f'Строка {i + 1}: Имя должно состоять минимум из 3х символов')

with open('errors.log', 'w') as errors_file:
    errors_file.write(errors_data)