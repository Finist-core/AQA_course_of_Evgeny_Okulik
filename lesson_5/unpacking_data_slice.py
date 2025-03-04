'''
Распаковка
Используется для  того, чтобы распределить элементы коллекции (список, словарь, множество,
кортеж)) по отдельным переменным.
Используется только в ситуациях, когда вы наверняка знаете количество элементов,
содержащихся в коллекции

print(list_1[-2:-6:-2])

первый  ([-2:]) - откуда начанать (первый элемент с конца под номером 1, а не ноль)
второй ([-6:]) - до куда считать (номер элемента до которого считаем не включительно)
третий ([-2]) - шаг с каким делать
'''
# Можно так, но много кода
my_list = [1, 3]
my_tuple = (2, 6, 9)
a = my_list[0]
b = my_list[1]
c = my_tuple[0]
d = my_tuple[1]
e = my_tuple[2]
print(a, b, c, d, e)

# Так сделает тоже самое, но меньше кода. Это и есть распаковка
a, b = my_list # Распаковка
c, d, e = my_tuple
print(a, b, c, d, e)

'''
Срез
Извлечение сраза позволяет взять из списка определенную его часть
'''
list_1 = [1, 3, 2, 5, 6, 7, 0]
print(list_1[1:3]) #Последний элемент не включительно 1 - 3 это 2, а не 3 элемента
print(list_1[:3]) # Чтобы распечатать с первого (0) элемента, можно его не ставить
print(list_1[3:]) # Чтобы распечатать до последнего элемента, можно его не ставить
print(list_1[1::2]) # Сделать срез с четвертого элемента до конца, с шагом 2 (3, 5, 7)
print(list_1[::-1]) # Так распечатаем список задом на перед
print(list_1[::-2]) # Так распечатаем список задом на перед, с шагом 2
print(list_1[-2:-6:-1]) # Распечатается со 2 с конца до 5 с конца
print(list_1[-2:-6:-2]) # Распечатается со 2 с конца до 5 с конца, с шагом 2

'''Методы строк
Со строками можно делать многое из того, что можно делать с другими коллекциями, т.к.
строка это по сути тоже коллекция - последовательность символов. Больше всего функциональность
строки похожа на функциональность кортежей. То есть со строками можно делать всё,
что их не ихменяет
'''

text = 'my long long string'
print(text[0]) # Так вытащим первую букву
print(len(text)) # Посчитает количество символов в строке
print(text.index('long')) # Покажет позицию первой буквы слова
print('long' in text) # Поиск в строке
print(text.count('long')) # Посчитать количество слов 'long' в переменной
print(text.count('n')) # Посчитать количество n в переменной
print(text.find('long')) # Как index, только если искать, то чего нет, то будет -1, а не ошибка
print((text[:7])) # Выведет первые 7 символов из переменной
print(text.startswith('my')) # Если текст начинается с того что ввели то True, нет - False
print(text.endswith('string')) # Если текст заканчивается на что ввели то True, нет - False



txt = 'ThIs tExT wItH MeSsed uP CaPiTaLiZaTiOn'
print(txt.capitalize()) # Делает первую букву предложения заглавной
print(txt.title()) # Делает каждую первую букву заглавной
print(txt.upper()) # Делает все буквы заглавными
print(txt.lower()) # Делает все буквы прописными
CaPiTaLiZaTiOn_index = txt.index('CaPiTaLiZaTiOn') # сделали переменныую
print(txt[:CaPiTaLiZaTiOn_index].lower() + txt[CaPiTaLiZaTiOn_index:].upper()) # Распечатали всё прописными,
# А переменную заглавными

#Если не знаем регистр в тексте, то можно так:
capitalize_index = txt.lower().index('capitalization') # Перевели весь текст в нижний регистр и ищем
print(txt[:capitalize_index].lower() + txt[capitalize_index:].upper())


msg = 'Hello world'
msg = msg.replace('world', 'univers') # replace не меняет переменную, поэтому надо переназначить
print(msg)


line = ('admin ')
line = line.strip() # Уберёт пробелы в начале и в конце
line = line.lstrip() # Уберёт пробелы слева
line = line.rstrip() # Уберёт пробелы справа
print(line)

line_1 = '"name"'
line_1 = line_1.strip('"') # Уберет выбраный символ
print(line_1)


'''
Строка в список, список в строку
'''

# Строка в список
my_string = 'some little text'
my_string_1 = 'some, little, text'
list_from_text = my_string.split() #Разделяем все слова на отдельные и делаем список, по пробелам
list_from_text_1 = my_string_1.split(",") #Разделяем все слова на отдельные и делаем список, по запятым
print(list_from_text)
print(list_from_text_1)

# Список в строку
progr = ['Java', 'Python', 'Ruby']
progr = ','.join(progr) # Соеденим слова из списка и разделим запятой
print(progr)

# Форматирование строки
a = 'one'
b = 'two'
print('First word is', a, ', second word is', b) # Ставит лишние пробелы

my_text = 'First woed is '  + a + ',  second word is ' + b # С методом конкотенации
print('First word is', a, ', second word is', b)

my_text = 'First word is %s, second word is %s' # %s обозначает места подстановки
print(my_text % (a, b)) # С помощью % подставляем кортеж (a, b) - способ устарел

# String format
my_text = 'First word is {}, second word is {}' # Символами {} обозначили где надо подставить
print(my_text.format(a, b)) # с помощью .format подставили

my_text = 'First word is {0}, second word is {1}' # Рекомендуется нумеровать, можно поменять позиции
print(my_text.format(a, b)) # с помощью .format подставили

# f-string
my_text = f'First word is {a}, second word is {b}' # более наглядный способ
print(my_text)