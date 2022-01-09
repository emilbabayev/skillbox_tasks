zen_file = open('zen.txt', 'r')

file_lines = list(zen_file)
file_lines.reverse()

for i_line in file_lines:
    print(i_line, end='')