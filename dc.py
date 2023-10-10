# Русский алфавит
russian_alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 
    'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 
    'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 
    'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
    ]

numeric = [11, 19, 15, 15, 2, 7, 6, 4, 18, 32, 14, 1, 18, 20, 16, 6, 8, 16, 19, 5, 20, 6, 19, 9, 14, 1, 22, 15, 12, 15, 5, 14, 20, 31, 3, 15, 5, 20, 19, 24, 11]
cArray = []

# Перевод из цифр в буквы
for i in range(len(numeric)):
    cArray.append(russian_alphabet[numeric[i] - 1])

print(cArray)


symbolic = ['а', 'б', 'в']
bArray = []

# Перевод из букв в цифры
for i in range(len(symbolic)):
    bArray.append(russian_alphabet.index(symbolic[i]) + 1)

print(bArray)