 # обработка исключений

a = 5
b = 2
f = 0
c = 'hello'
try:
    d = a + c
except TypeError:
    print('разные типы данных - error')
except ZeroDivisionError:
    print('делить на 0 нельзя - Error')
else:
    print('если в try нет ошибок то это сообщение будет видно')
finally:
    print("данный блок Finally, если прописан, то будет выводиться всегда последним")

