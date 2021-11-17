students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },

    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },

    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dictionary):
    all_interests = []
    all_surnames = ''
    for i_person, i_info in dictionary.items():
        all_interests.append(i_info['interests'])
        all_surnames += i_info['surname']

    return all_interests, len(all_surnames)


for i_student, i_info in students.items():
    print(i_student, '-',  i_info['age'])

interests, surnames_length = f(students)
print('Интересы: {list}\n'
      'Общая длина всех фамилий: {int}'.format(
        list=interests,
        int=surnames_length
))

