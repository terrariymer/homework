# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for i in word:
    if i in "цкншщзхфвпрлджчсмтб":
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(" ")))


# Вывести первую букву каждого слова на отдельной строке
for i in sentence.split():
    print(i[:1])
print(*[i[:1] for i in sentence.split()], sep='\n')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
