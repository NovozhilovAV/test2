# CREATE TABLE homes(       #Создали таблицу в pgAdmin
# 	id SERIAL Primary Key,
# 	house int,
# 	appartment int,
# 	flor int,
# 	area real,
# 	room int,
# 	ready bool,
# 	finishing bool,
# 	balcon bool,
# 	checkin bool,
# 	titelpeople text
# )

# Insert Into homes (id, house, appartment,
# flor, area, room, ready, finishing, balcon,
# checkin, titelpeople) Values      # Заполнили таблицу данными
# (DEFAULT,1,1,1,51,2, True, True, False, True, 'Ivanov'),
# (DEFAULT,1,2,1,42,1, True, True, False, True, 'Petrov'),
# (DEFAULT,1,3,1,43,1, True, True, False, True, 'Sidorov'),
# (DEFAULT,1,4,1,44,2, True, True, False, True, 'Smirnov'),
# (DEFAULT,1,5,2,52,2, True, True, True, True,'/'),
# (DEFAULT,1,6,2,42,1, True, True, False, True, '/'),
# (DEFAULT,1,7,2,43,1, True, True, False, True, '/'),
# (DEFAULT,1,8,2,44,2, True, True, False, True, '/')

# Update homes      # Отредактировали таблицу
# Set checkin = 'False'
# WHERE titelpeople = '/'

# Update homes
# Set balcon = 'True'
# Where checkin = 'False'




# открываем библиотеку в этом файле
import psycopg2
# создаем объект для подключения к БД
connect1 = psycopg2.connect(
    dbname='postgres',
    host='localhost',  # 127.0.0.1 - или так то место где лежит база данных
    port=5432,  # порт для подключения
    user='postgres',
    password='postgres'
)
# Создадим функцию просмотра свободных квартир
def freeHouse():
    cursor1 = connect1.cursor()    # подключаемся БД и ставим курсор в начало ввода
    # формируем запрос
    cursor1.execute("SELECT appartment FROM homes WHERE checkin = 'False'")
    # Выгружаем все данные в перенменную дата1
    data1 = cursor1.fetchall()
    cursor1.close()  # закрыли окошко ввода
    return data1

# print(freeHouse())  # Вызвали функцию - ok-работает

# def seelHouse():
#     cursor1 = connect1.cursor()
#     cursor1.execute("Select * From homes WHere ready = 'True' AND finishing = 'True' AND titelpeople = '/'")
#     data1 = cursor1.fetchall()
#     cursor1.close()
#     return data1
#
# print(seelHouse())

def buy():
    print('Какой номер квартиры вы выбираете?')
    appartment = int(input())
    print('Какой этаж вы выбираете?')
    flor = int(input())
    cursor1 = connect1.cursor()
    cursor1.execute('SELECT appartment, flor FROM homes')  # забераем все продукты из БД
    data1 = cursor1.fetchall()  # все названия соков
    print(data1)
    print(type(data1))
    cursor1.close()

    isFindAppart = False  # переменная сигнализирует есть ли там существующая позиция
    for i in data1:
        if i[0] == appartment:
            isFindAppart = True
    for j in data1:
        if j[1] == flor:
            isFindFlor = True


    if isFindProduct == False:
        addNewProduct(product)  # пeредаем продукт так как уже задали его название
    else:
        editValueOfProduct(product)
