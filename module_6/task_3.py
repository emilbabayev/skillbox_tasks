print('Начался восьмичасовой рабочий день.')

hour = 1
tasks = 0
answer_to_wife = False

while hour != 9:
    print(f'{hour}-й час')
    tasks += int(input('Сколько задач решит Максим? '))
    if not answer_to_wife:
        answer_to_wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    hour += 1
print(f'Рабочий день закончился. Всего выполнено задач: {tasks}')