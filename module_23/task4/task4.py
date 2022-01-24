reg_good_data = ''
reg_bad_data = ''


def check_valid(data):
    is_valid = False
    user_name, user_mail, user_age = user_data[0], user_data[1], user_data[2]

    if len(data) != 3:
        raise IndexError
    elif not user_name.isalpha():
        raise NameError
    elif not ('@' in user_mail and '.' in user_mail):
        raise SyntaxError
    elif not (10 <= int(user_age) <= 99):
        raise ValueError
    else:
        is_valid = True

    return is_valid


with open('registrations.txt', 'r') as reg_file:
    for i, line in enumerate(reg_file):
        try:
            user_data = line.split()
            if check_valid(user_data):
                reg_good_data += f'{line}'

        except IndexError:
            error_text = f'Строка {i + 1}: Отсутствуют некоторые данные'
            print(error_text)
            reg_bad_data += f'{line[0:-1]} - {error_text}\n'
        except NameError:
            error_text = f'Строка {i + 1}: Имя может состоять только из букв алфавита'
            print(error_text)
            reg_bad_data += f'{line[0:-1]} - {error_text}\n'
        except SyntaxError:
            error_text = f'Строка {i + 1}: E-mail введен неверно'
            print(error_text)
            reg_bad_data += f'{line[0:-1]} - {error_text}\n'
        except ValueError:
            error_text = f'Строка {i + 1}: Возраст введен неверно'
            print(error_text)
            reg_bad_data += f'{line[0:-1]} - {error_text}\n'


with open('registrations_good.log', 'a', encoding='utf-8') as reg_good:
    reg_good.write(reg_good_data)
with open('registration_bad.log', 'a', encoding='utf-8') as reg_bad:
    reg_bad.write(reg_bad_data)