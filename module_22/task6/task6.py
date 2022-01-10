alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_upper = [sym.capitalize() for sym in alphabet_lower]


new_text = ''
text_file = open('text.txt', 'r')

for i_line, line in enumerate(text_file):
    for sym in line:
        if sym.isalpha() and sym.islower():
            new_text += alphabet_lower[(alphabet_lower.index(sym) + i_line + 1) % len(alphabet_lower)]
        elif sym.isalpha() and sym.isupper():
            new_text += alphabet_upper[(alphabet_upper.index(sym) + i_line + 1) % len(alphabet_upper)]
    new_text += '\n'

text_file.close()

ciphertext_file = open('cipher_text.txt', 'w')
ciphertext_file.write(new_text)
ciphertext_file.close()