'''
Распаковка
Используется для  того, чтобы распределить элементы коллекции (список, словарь, множество,
кортеж)) по отдельным переменным.
Используется только в ситуациях, когда вы наверняка знаете количество элементов,
содержащихся в коллекции
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
