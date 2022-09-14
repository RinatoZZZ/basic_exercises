# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print('--------------------')

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))
print('--------------------')

# Вывести количество гласных букв в слове
word = 'Архангельск'
letters = 'аяеэоёиуюы'
for i in  word.lower():
    if i in letters:
        print(i)

print('--------------------')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print('--------------------')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
word_list = sentence.split()
for first in word_list:
    print(first[0])
print('--------------------')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
average_string_len = 0
word_list = sentence.split()
for words in word_list:
    average_string_len += len(words)
print(f'Усредненая длина слова: {int(average_string_len/len(word_list))}')