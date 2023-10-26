# Открываем библиотеку в этом файле
import psycopg2
# Создаем объект для подключения к БД
connect1 = psycopg2.connect(
    dbname='postgres',
    host='localhost',  # 127.0.0.1 - или так то место где лежит база данных
    port=5432,  # порт для подключения
    user='postgres',
    password='postgres'
)
# подключает БД и в окне ввода устанавливает курсор в начало ввода
cursor1 = connect1.cursor()  # формируем запрос

cursor1.execute('SELECT * FROM people')  # execute - наполнение строки и отправка

data1 = cursor1.fetchall()    # Выгружаем все данные в перенменную дата1
print(data1)

# cursor1.execute("INSERT INTO people VALUES ('Python', 'python1', 35, 'SaintP')") - можно писать и так

cursor1.execute("INSERT INTO people VALUES"
                " ('Python', 'python1', 35, 'SaintP')")
connect1.commit()  # применение заполненых данных

cursor1.execute('SELECT * FROM people')  # execute - наполнение строки и отправка

data1 = cursor1.fetchall()    # Выгружаем все данные в перенменную дата1
print(data1)

cursor1.close()    # закрыли окошко ввода

connect1.close()    # закрыли соединение


# смотрим все данные таблицы
# Необходимо написать программу, которая имитирует электронную кассу продуктового магазина.
# заводим таблицу (через pgAdmin) с полями id SERIAL,текст товара,целое число цены,реальный вес,целое значение товара
# Необходимые функции реализации продажи товара (def sell(product, value)), закупки товара (def sell(product, value)),
# подсчета кассы (def countcash())
