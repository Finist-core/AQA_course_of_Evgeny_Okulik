'''
Условия и цыклы
if
elif
else

for
while
'''
from cloudinit.distros.ug_util import extract_default
from pygments.lexer import words

# Условия - conditions

# Пример 1
user_input = int(input('your number: '))

if user_input == 1:
    print('One')
elif user_input == 2:
    print('Two')
else:
    print('Many')

# Пример 2 Так не надо, проверяет всё, программа работает дольше
user_input = int(input('your number: '))

if user_input == 1:
    print('One')
if user_input == 2:
    print('Two')
if user_input not in [1, 2]:
    print('Many')

# Пример 3 Так делаем условие, что надо ввести число
user_input = input('your number: ')
if user_input.isnumeric(): # .isnumeric() условие, что ввод число
    user_input = int(user_input)
    if user_input == 1:
        print('One')
    elif user_input == 2:
        print('Two')
    else:
        print('Many')
else:
    print('Please enter a number')

# Loops - Циклы

# Пример 1 Распечатать коллекцию
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']
for name in names: # Для каждого имени из имён, распечатать
    print(name)

# Пример 2 Распечатать только имена на J
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']

for name in names:
    if name.startswith('J'):
        print(name)

# Пример 3 Распечатать имена, а к именам на J, добавить обращение Mr. end=' ' не даст вставить перенос строки
# Так же можно с кортежами и множествами
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']

for name in names:
    if name.startswith('J'):
        print('Mr.', end=' ')
    print(name)

# Пример 4 Если использовать словарь с помощью for, получим, только ключи
names = {'John': 132, 'Tom': 110, 'James': 100}
for name in names:
    print(name)

names = {'John': 132, 'Tom': 110, 'James': 100}
for name in names.keys(): # Получим, тоже что и без .keys
    print(name)

# Пример 5 Можно получить только значения
names = {'John': 132, 'Tom': 110, 'James': 100}
for name in names.values(): # Получим только значения
    print(name)

# Пример 6 Методом f-string можно получить ключ и значение
names = {'John': 132, 'Tom': 110, 'James': 100}
for name in names:
    print(f'{name}: {names[name]}') # Двоеточие здесь значит само двоеточие при выводе

# Пример 7 Ещё вывод ключ и значение
names = {'John': 132, 'Tom': 110, 'James': 100}
print(names.items()) # Выведет кортежи ключ: значение
for name in names.items(): # Выведет кортежи по очереди
    print(name)

# Пример 8 Вывод ключ - значение, как должно быть
names = {'John': 132, 'Tom': 110, 'James': 100}
for name in names.items():
    name, height = name # Распаковка словаря, переменная name - ключ, height - значение
    print(f'{name}: {height}')

# Пример 9 А так ещё лучше и понятнее
names = {'John': 132, 'Tom': 110, 'James': 100} # Словарь
for name, height in names.items(): # задаём ключу переменную name, значению height, ищем по
    print(f'{name}: {height}') # в f-string первым вставляем ключ, вторым значение

# Пример 10 Как вывести все только слова с буквой О
text = 'English texts for beginners to practice reading and comprehension online and for free.'
for word in text.split() : # .split разделет предложение на слова
    if "o" in word:
        print(word)

# Пример 11 Убрать слова с буквой О
text = 'English texts for beginners to practice reading and comprehension online and for free.'
for word in text.split():
    if 'o' in word:
        pass
    else:
        print(word, end=' ')

# Пример 12 Распечатать все слова с О в столбик, а затем вывести оставшееся предложение
text = 'English texts for beginners to practice reading and comprehension online and for free.'
fin_text = []
for word in text.split():
    if 'o' in word:
        print(word)
    else:
        fin_text.append(word)
print(' '.join (fin_text))