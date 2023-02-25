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
# # подключает БД и в окне ввода устанавливает курсор в начало ввода
# cursor1 = connect1.cursor()
#
# # формируем запрос
# cursor1.execute('SELECT * FROM shop')  # execute - наполнение строки и отправка
# # Выгружаем все данные в перенменную дата2
# data1 = cursor1.fetchall()
# print(data1)    #
# # print(type(data1))


# def sell(haveProduct, countProduct):
#     haveProduct = input('Что для вас ?')
#     countProduct = int(input('Сколько ?'))
#     cursor1.execute(f"UPDATE shop SET balance = balance - {countProduct} WHERE product = {haveProduct}")
#     connect1.commit()    # применение заполненых данных
#     # print('')


# cursor1.execute('SELECT * FROM shop')  # execute - наполнение строки и отправка
# # Выгружаем все данные в перенменную дата3
# data3 = cursor1.fetchall()
# print(data3)



# =========================


# def buy(product, bd_targ, value): # принимаемые функцией значения
#    cursor1 = bd_targ.cursor()  # Очищаем поле ввода
#    cursor1.execute(f"SELECT * FROM shop WHERE product = '{product}'")  # Выполняем запрос в формате fстр. (все записи со всеми полями, где продукт = продукт)
#    data1 = cursor1.fetchall()  # Выгрузка результатов сгенерированного запроса в базе данных
#    if data1 == []:
#       infoofprice = int(input('Введите цену товара: '))
#       infoofweight = float(input('Введите объем: '))
#       cursor1.execute("SELECT MAX(id) FROM shop")
#       data1 = cursor1.fetchall()
#       max_id = data1.pop()
#       id = max_id[0] + 1
#       cursor1.execute(f"INSERT INTO shop VALUES ({id}, '{product}',{infoofprice}, {infoofweight}, {value})") # max_id[0] обращаемся к значению внутри объекта по индексу
#       #   cursor1.execute(f"INSERT INTO shop ({id}, '{product}',{infoofprice}, {infoofweight}, {value})") VALUES  # не надо будет обращаться к id
#       bd_targ.commit()
#    else:
#       newvalue = data1.value + 1
#       cursor1.execute(f"UPDATE shop SET value = {newvalue} WHERE product = '{product}'")
#       bd_targ.commit()
#
# price = input('Введите количество товара: ')
# search = input('Введите название товара: ')
# buy(search, bd, price)


# connect1 = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="postgres",
#     host="127.0.0.1",
#     port="5432"
# )

STARTCASH = 10000000


def showTable():
    cursor1 = connect1.cursor()
    cursor1.execute('SELECT product, prise, widht, balance FROM shop')
    data1 = cursor1.fetchall()
    cursor1.close()
    return data1


def countCash():
    cursor1 = connect1.cursor()
    cursor1.execute('SELECT price, balance FROM shop')
    data1 = cursor1.fetchall()  # 180/500 - 170/300
    cursor1.close()
    print(type(data1))
    print(data1)  # 180/500 - 170/300

    summa = 0
    for i in data1:
        summa += i[0] * i[1]

    return STARTCASH - summa


def addNewProduct(product):
    newPrice = int(input('Введите цену товара: '))
    newWeight = float(input('Введите объем товара: '))
    newValueOfProduct = int(input('Введите кол-во товара: '))
    cursor1 = connect1.cursor()
    cursor1.execute(f"INSERT INTO shop (product, prise, widht, balance) VALUES"
                    f" ('{product}', {newPrice}, {newWeight}, {newValueOfProduct}")
    print(f"Привезли '{product}', по: {newPrice}, объемом: {newWeight}, в кол-ве: {newValueOfProduct}")
    data1 = cursor1.fetchall()
    cursor1.close()
    print(data1)


def editValueOfProduct(product):
    print('Сколько привезли товара? ')
    newValue = int(input('Введите кол-во товара: '))
    cursor1 = connect1.cursor()
    cursor1.execute(f"UPDATE shop SET balance = {newValue} WHERE {product}")

    print(f"Привезли '{product}', по: {newPrice}, объемом: {newWeight}, в кол-ве: {newValueOfProduct}")
    data1 = cursor1.fetchall()
    cursor1.close()
    print(data1)


def buy():
    print('Какой продукт привезли?')
    product = input()
    cursor1 = connect1.cursor()
    cursor1.execute('SELECT product FROM shop')  # забераем все продукты из БД
    data1 = cursor1.fetchall()  # все названия соков
    print(data1)
    # print(type(data1))
    cursor1.close()

    isFindProduct = False  # переменная сигнализирует есть ли там существующая позиция
    for i in data1:
        if i[0] == product:
            isFindProduct = True

    if isFindProduct == False:
        addNewProduct(product)  # пeредаем продукт так как уже задали его название
    else:
        editValueOfProduct(product)


def sell():    # продажа товара
    sellProduct = input('Что продать? ')
    sellValProd = int(input('сколько? '))
    cursor1 = connect1.cursor()
    cursor1.execute(f"UPDATE shop SET balance = balance - {sellValProd} WHERE product = '{sellProduct}'")
    connect1.commit()  # применение заполненых данных
    #
    cursor1.close()  # закрыли окошко ввода
    print(f"Ваш товар '{sellProduct}'в количестве {sellValProd} продан ! ")

# sell()  # работает  но надо прописать цену

# buy()

# print(countCash())


# функция которая дает нам выбор что делаем принимаем/продаем/добавляем/изменяем
def main():
    while True:
        print('Для информации о складе жмем 1 \n Для пополнения склада жмем 2 \n Для продажи товара жмем 3 ')
        a = int(input())     #
        match a:
            case 1:
                print(showTable())
            case 0:
                break
            case 2:
                print(buy())
            case 3:
                print(sell())


main()

# buy()

# print(showTable())

# print(countCash())

connect1.close()
