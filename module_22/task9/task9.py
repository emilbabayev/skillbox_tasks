import collections
import zipfile
import os


def unzip(archive):
    z_file = zipfile.ZipFile(archive, 'r')
    for i_file in z_file.namelist():
        z_file.extract(i_file)


def make_stat(file):
    char_dict = collections.OrderedDict()

    for i_line in file:
        for i_char in i_line:
            i_char = i_char.lower()
            if i_char.isalpha():
                if i_char not in char_dict:
                    char_dict[i_char] = 1
                char_dict[i_char] += 1
    return char_dict


def sort_stat(statistic):
    sorted_statistic = collections.OrderedDict()
    sorted_values = sorted(statistic.values(), reverse=True)
    for value in sorted_values:
        for key in statistic:
            if statistic[key] == value:
                sorted_statistic[key] = value

    return sorted_statistic


def print_stat(statistic):
    print('{:-^21}'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('Буква', 'Кол-во'))
    print('{:-^21}'.format('+'))

    for i_char, i_count in statistic.items():
        print('|{: ^9}|{: ^9}|'.format(i_char, i_count))

    print('{:-^21}'.format('+'))


unzip('voyna-i-mir.zip')

f = open('voyna-i-mir.txt', 'r', encoding='utf-8')

stat = make_stat(f)
sorted_stat = sort_stat(stat)
print_stat(sorted_stat)

f.close()
