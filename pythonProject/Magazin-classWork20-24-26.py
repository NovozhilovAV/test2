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

COUNTCASH = 10000000    # касса магазина с начальной суммой

def shopTable():  # функция инвентаризации - показали все товары и их количество
    cursor1 = connect1.cursor()  # подключает БД и в окне ввода устанавливает курсор в начало ввода
    # формируем запрос
    cursor1.execute('SELECT product, prise, weight, valueofproduct FROM magazin')
    # Выгружаем все данные в перенменную дата1
    data1 = cursor1.fetchall()
    cursor1.close()  # закрыли окошко ввода
    return data1

# print(shopTable())  # Вызвали функцию


def countCash():    # подсчет кассы
    cursor1 = connect1.cursor()  # подключает БД и в окне ввода устанавливает курсор в начало ввода
    # формируем запрос
    cursor1.execute('SELECT prise, valueofproduct FROM magazin')
    # Выгружаем все данные в перенменную дата2
    data1 = cursor1.fetchall()
    cursor1.close()  # закрыли окошко ввода
    print(data1)  # количество товара и цена
    print(type(data1))

    summa = 0
    for i in data1:  # проходим циклом по всему списку кортежу дата1. в котором цена и количество
        summa += i[0]*i[1]  # складываем количество - первое число умножаем на втoрое

    return COUNTCASH - summa


def addNewProduct(product):  # Получение нового товара
    productNewCash = int(input('товар по какой цене привезли?'))
    productNewValue = int(input('какое количество товара привезли?'))
    productNewWeight = float(input('Какой объём/в чем продавать еденицу товара,шт,кг,0.5/  товара привезли?'))
    cursor1 = connect1.cursor()
    cursor1.execute(f"INSERT INTO magazin (product, prise, weight, valueofproduct) VALUES"
                    f" ('{product}', {productNewCash}, {productNewWeight}, {productNewValue})")

    print(f"Товар '{product}' в количестве  {productNewValue} объёмом {productNewWeight} по цене {productNewCash} принят")
    connect1.commit()    # применение заполненых данных
    cursor1.close()  # закрыли окошко ввода




def editValueOfProduct(product):    # Добавление нового товара
    productOfValue = int(input('какое количество товара привезли?'))
    cursor1 = connect1.cursor()
    cursor1.execute(f"UPDATE magazin SET valueofproduct = valueofproduct + {productOfValue} WHERE product = '{product}'")

    cursor1.execute(f"SELECT valueOfProduct FROM magazin WHERE product = '{product}'")
    connect1.commit()  # применение заполненых данных
    data1 = cursor1.fetchall()



def buy():     # привоз товара
    print('какой продукт привезли: ')
    product = input()
    cursor1 = connect1.cursor()
    cursor1.execute('SELECT product FROM magazin')
    # Выгружаем все данные в перенменную дата1
    data1 = cursor1.fetchall()  # water, beer.....
    cursor1.close()  # закрыли окошко ввода
    print(data1)
    print(type(data1))
    cursor1.close()  # закрыли окошко ввода
# проверяем условие- есть этот товар(да/нет) и добаавлям или обновляем данные

    isFineProduct = False
    for i in data1:
        if i[0] == product:
            isFineProduct = True

    if isFineProduct == False:
        addNewProduct(product)      # Получение нового товара

    else:
        editValueOfProduct(product)     # Добавление нового товара



def sell():    # продажа товара
    sellProduct = input('Что продать? ')
    sellValProd = int(input('сколько? '))
    cursor1 = connect1.cursor()
    cursor1.execute(f"UPDATE magazin SET valueofproduct = valueofproduct - {sellValProd} WHERE product = '{sellProduct}'")
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
                print(shopTable())
            case 0:
                break
            case 2:
                print(buy())
            case 3:
                print(sell())


#  доделать завершение цикла и сделать подсчет денег в кассе
main()

connect1.close()