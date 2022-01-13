numbers_file = open('numbers.txt', 'r')
result = 0

for i_line in numbers_file:
    if i_line.strip():
        result += int(i_line.strip())

numbers_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(result))
answer_file.close()
