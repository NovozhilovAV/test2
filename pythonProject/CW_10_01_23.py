#  сортировка
#  1 пузырьковая - сравниваем пары чисел и
#  наименьшее число становиться первым и таким образом сортируем весь список.

startList = [6, 8, 4, 5, 1, 3, 2]

for i in range(0,len(startList) - 1, 1):
     for j in range(0, len(startList) - i - 1, 1):
         if startList[j] > startList[j + 1]:
             startList[j], startList[j + 1] = startList[j + 1], startList[j]

print(startList)

  # сортировка вставками


  # сортировка Shella
a = [3, 16, 7, 18, 0, 1, 6, 14, 45, 11, 5]



