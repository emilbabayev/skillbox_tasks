from alphabet_detector import AlphabetDetector
ad = AlphabetDetector()

f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
print(f'Содержимое файла text.txt:\n{data}\n')
f.close()

data = data.lower().replace(' ', '')

latin_char_dict = dict()
latin_char_count = 0
for sym in data:
    if sym.isalpha() and ad.is_latin(sym):
        if sym in latin_char_dict:
            latin_char_dict[sym] += 1
            latin_char_count += 1
        else:
            latin_char_dict[sym] = 1
            latin_char_count += 1


result = ''
frequency_analysis = dict()
for char, count in latin_char_dict.items():
    freq = round(count / latin_char_count, 3)
    if freq in frequency_analysis:
        frequency_analysis[freq].append(char)
    else:
        frequency_analysis[freq] = list()
        frequency_analysis[freq].append(char)

freq_sorted = sorted(frequency_analysis.keys(), reverse=True)

for freq in freq_sorted:
    for char in sorted(frequency_analysis[freq]):
        result += f'{char} {freq}\n'

analysis_file = open('analysis.txt', 'w')
analysis_file.write(result)
analysis_file.close()

analysis_file = open('analysis.txt', 'r')
analysis_data = analysis_file.read()
print(f'Содержимое файла analysis.txt:\n{analysis_data}')
analysis_file.close()