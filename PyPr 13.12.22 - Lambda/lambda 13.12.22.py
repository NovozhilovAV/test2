# рекурсия -
# Вызвали функцию внутри функции
# n = 10
# def lalala(arg1):
#     print('Число равно' + str(arg1))
#     if n > 6:
#         lalala(arg1 - 1)
# lalala(n)
# print(lalala)


# Анонимная функция - лямбда выражение(функция)

# 1. Найти наибольший элемент списка (for, if)
# 2. Отсортировать список и сделать из него кортеж
# 3. Сделать 2 множества по 7 элементов
# Первое - это первые 7 чисел, которые делятся 3
# Второе - это первые 7 чисел, которые делятся 5
# Получить их пересечение (И) и все символы (ИЛИ)
# 4. Объявить словарь на 4 пары. Получите коллекцию всех значений,
# коллекцию всех ключей, пару под индексом 2
# 5. Напишите рекурсивную функцию (с одним аргументом), которая
# считает факториал
# 6. Напишите лямбда-функцию, которая принимает коллекцию
# и считает для каждого её элемента его остаток от деления на 3
# 7. Напишите лямбда-функцию, которая принимает коллекцию и
# фильтрует её элементы на предмет деления значения элемента
# коллекции на 5 нацело
# 8. Напишите лямбда-функцию, которая принимает коллекцию и
# ищет в этой коллекции самую короткую строку

# a = [2, 3, 35, 21, 2]  # создали список
# 1
# for el in a:

# 2 Отсортировать список и сделать из него кортеж
# a.sort()
# b = tuple(a)
# print(b)
# print(type(b))

# 3 Сделать 2 множества по 7 элементов
# Первое - это первые 7 чисел, которые делятся 3
# Второе - это первые 7 чисел, которые делятся 5
# Получить их пересечение (И) и все символы (ИЛИ)


# 6. Напишите лямбда-функцию, которая принимает коллекцию
# и считает для каждого её элемента его остаток от деления на 3

# 7Напишите лямбда-функцию, которая принимает коллекцию и
# фильтрует её элементы на предмет деления значения элемента
# коллекции на 5 нацело
# a = [2, 3, 35, 21, 2]
# b = list(filter(lambda x: x % 5 == 0, a))
# print(b)

# 8. Напишите лямбда-функцию, которая принимает коллекцию и
# ищет в этой коллекции самую короткую строку


