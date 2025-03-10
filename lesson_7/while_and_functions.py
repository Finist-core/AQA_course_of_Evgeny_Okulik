'''
while loop - цикл while

Functions - функции
'''

# while

# Пример 1 Простой пример, который распечатает слово Hello пять раз
i = 0

while i < 5:
    print('Hello')
    i += 1

# Пример 2 Как остановить программу
while True:
    user_input = input('Enter something')
    if user_input == 'exit':
        break                               # С помощью break, останавливаем программу
    elif user_input == 'skip':
        print('skipping')
        continue                            # С помощью continue останавливаем текущий шаг, программа работает дальше
    elif len(user_input) > 10:
        print('Your input is too long')
    else:
        print("It`s OK")
print('Good bye!')

# Пример 3
text = 'English texts for beginners to practice reading and comprehension end online and for free.'

words = text.split()
fin_words = []
for word in words:
    if word == 'end':
        break           # Так остановим работу программы, когда условие выполненоЫ
    elif 'o' in word:
        print(word)
        continue        # С помощью этого, если нашёл О в слове, цикл прирывается и начанается с начала
    fin_words.append(word)
print(' '.join(fin_words))

'''
Functions - функции
Это самые основные программные структуры в языке Python, позволяющие многократное использование
программного кода и уменьшающие его избыточность. Так же позволяют разбить сложную систему 
на достаточно простые и легко управляемые части. Они могут принимать агрументы и возвращать
результаты выполнения.
DRY - don`t repeat yourself - не повторяйся
'''

# Пример 1 Функция, которая ждет данные и что-то делает
# Как делать не надо

a = 1
b = 5
c = 4
d = 7
y = 5

main_number = 47

print(a + main_number)
print(b + main_number)
print(c + main_number)
print(d + main_number)
print(y + main_number)

# Как надо
a = 1
b = 5
c = 4
d = 7
y = 5

main_number = 47

def calc(numb): # В скобках написано, что сюда надо что-то передать, они попадут в numb, работает только внутри функции
    print(numb + main_number)

calc(a)

# Пример 2
# Как не надо

a = 1
b = 5
c = 4
d = 7
y = 1

main_number = 47

if y == 0:
    print(a)
else:
    print(a + main_number)
if y == 0:
    print(b)
else:
    print(b + main_number)
if y == 0:
    print(c)
else:
    print(c + main_number)
if y == 0:
    print(d)
else:
    print(d + main_number)

# Как надо с помощью функции
a = 1
b = 5
c = 4
d = 7
y = 1

main_number = 47


def calc(numb):
    if y == 0:
        print(numb)
    else:
        print(numb + main_number)

calc(a)
calc(b)
calc(c)
calc(d)

# Пример 3 Функция, которая ни чего не делает return.
# Просто возвращает результат, а что с ним делать решает программист

a = 1
b = 5
c = 4
d = 7
y = 1

main_number = 47


def calc(numb): # в скобках пишем параметры, которые может принять функция
    if y == 0:
        return
    else:
        result = numb + main_number # Обычно переменную для одно использования не создают
        return result

print(calc(a))     # Тут распечатается (в скобках аргумент, который применяем)
result_b = calc(b) # Тут результат добавится в переменную result_b
calc(c)            # Тут ни чего не распечатается
calc(d)            # Тут ни чего не распечатается

def print_words(first, second, third, fourth, fifth):
    print(f'The firrst word is {first}, second word is {second},{third}, {fourth}, {fifth}')

# Так питон расставит по порядку
print_words('one', 'two', 'three', 'four', 'five')

# Так сами говорим в какой параметр подставлять какой аргумент
print_words(fifth='five', third='three', fourth='four', first='one', second='two')

# Пример 4 функция с дефолтным параметром (в примере - это вторая степень)

def power(number, degree=2):
    return number ** degree
print(power(2)) # так возведем 2 в квадрат
print(power(2, 3)) # А так поменяем дефолтную степень на третью

def example(e, f, g, ff='one', gg='two'):
    print(e, f, g, ff, gg)
example(2, 3, 5) # можно менять любой параметр, например gg=1

# Пример 5 Функция может принимать любое количество неименованных позиционных аргументов
def sum_all(*args): # args написано, потому что так принято писать
    print(args)

sum_all(1, 4, 6) # при передаче аргументов, они превращаются в кортеж


def sum_all(*args): # Просто пример, есть функция sum, которой можно воспользоваться так: numb = (10,10,10) print(sum(numb))
    result = 0
    for x in args:
        result += x
    return result

print(sum_all(1, 10, 12, 100))

# Пример 6 Функция, которая принимает любое количество именованных позиционных аргументов
# Эта функция вызывает по одному
def price_list(title, price):
    print(f'Product {title} price is {price}')

price_list('iphone', 2500)

#
def price_list(**kwargs): # **kwargs когда ждут неограниченное количество аргументов
    for title, price in kwargs.items():
        print(f'Product {title} price is {price}')

price_list(iphone=2500, laptop=150, samsung=2000) # создаст словарь (ключ-значение)

'''ВАЖНО!!! Сначала позиционные, потом неограниченные количества, позиционные именованные, 
именованные неограниченное количество, то есть так:
def price_list(list_title, *agrs, defoult_qty=234, **kwargs)
'''