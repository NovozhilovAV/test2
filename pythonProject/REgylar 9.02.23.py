import re

# РЕгулярные выражения

# a = r'Hello \n Word'
#
# print(a)
# print(type(a))
#
# c = 'И снова \nЗдравствуйте'
# print(c)
#
# b = re.findall(r'Пусть всегда', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(b)
#
# d = re.findall(r'\w+', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(d)
#
# e = re.findall(r'\w*', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(e)
#
# g = re.findall(r'\d+', "Пусть всег35да бу7дет со88лнце!!, Пусть всегда буду я")
# print(g)
#
# e1 = re.findall(r'вс...а', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(e1)       # символ .
#
# e2 = re.findall(r'да.бу', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(e2)
#
# e3 = re.findall(r'\s', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(e3)    # выведет все пробелы

# e4 = re.findall(r'\b', "Пусть всегда будет солнце!!, Пусть всегда буду я")
# print(e4)     # начало и конец слова

# e5 = re.findall(r'[0-9]', "hugyihgd3456788987tnh78th5e56")
# print(e5)

# e6 = re.findall(r'[0-9][a-z]', "hugyihgd3456788987tnh78th5e56")
# print(e6)      # ['7t', '8t', '5e']  - цифры и буквы в нижнем регистре
# #
# e6 = re.findall(r'[a-zA-Z]\d', "hugyihgd3456g7L88I987tnh78th5e56")
# print(e6)      #['d3', 'g7', 'L8', 'I9', 'h7', 'h5', 'e5']

# e6a = re.findall(r'[^g]\d', "hugyihgd3456g7L88I987tnh78th5e56")
# print(e6a)

# e7 = re.findall(r'[^I]\d', "hugyihgd3456g7L88I987tnh78th5e56")
# print(e7)    # этого символа не должно быть I
#
# e6b = re.findall(r'[^o][^I]\d', "hugyihhgd3456g7L88I987tnh78t88h5e56")
# print(e6b)
#
# e6c = re.findall(r'h{3}', "hugyihhhgd3456g7L88I987tnhhh78th5e56")
# print(e6c)

# e6 = re.findall(r'8.h5', "hugyihgd3456g7L88I987tnh78th5e56")
# print(e6)

# e61 = re.findall(r'8.eh{3}', "hugyihgd3456g7L88I987tnh78tehhh5e56")
# print(e61)    # ['8tehhh']
#
# e61 = re.findall(r'h{,3}', "hugyihgd3456g7L88I987tnh78tehhh5e56")
# print(e61)    # ['h', '', '', '', '', 'h', '', .... 'hhh'....]
#
# e611 = re.findall(r'h{3}', "hugyihgd3456g7L88I987tnh78tehhh5e56")
# print(e611)    # ['hhh']
#
# e612 = re.findall(r'h{2,}', "hugyihhhgd345hh6g7L88I987tnh78tehhh5e56")
# print(e612)     # ['hhh', 'hh', 'hhh']
#
# e613 = re.findall(r'h{1,3}', "hugyihgd3456g7L88I987tnh78tehhh5e56")
# print(e613)     # ['h', 'h', 'h', 'hhh']

e614 = re.findall(r'\d\d\d', "hugyihgd3456g7L88I987tnh78tehhh5e56")
print(e614)    #  ['345', '987']

e615 = re.findall(r'\d\d\d|\d\d', "hugyi358hgd3456g7L88I987tnh78tehh158h5e56")
print(e615)    #  ['345', '987']


# e6 = re.split(r"8", "hugyihgd3456g7L88I987tnh78th5e56")
# print(e6)


# a = re.sub(r"Москву", "Пермь", "Я люблю Москву")
# print(a)
#
# b = re.sub(r'-\d', '!!!&&&!!!', 'sdvfs-sdfe89657-87shg78hf')
# print(b)        # заменяет выражение на !!... после того как встретит цифру после -


# создали файл с текстом 82.тхт - открыли- прочитали-нашли номера- закрыли

x = open('82.txt', encoding='utf-8')
y = x.read()

# y = re.findall(r'[А-Я].[А-Я0-9][А-Я0-9]\d+', y)
# y = re.findall(r'[А-Я].[А-Я0-9][А-Я0-9]\d{,4}', y)   # \d{,4} - цифры до 4 знаков

# print('номера = ', y)
# номера =  ['А-МР77', 'К-МР77', 'Р-МР77', 'О-МР77',
# 'В-МР77', 'М-МР77', 'Т-МР77', 'А-КР177', 'В-КР177',
# 'К-КР177', 'Е-КР177', 'Х-КХ77', 'К-ОО77', 'Е-РЕ177',
# 'А-МО77', 'А-МО99', 'А-ОО77', 'В-ОО77', 'М-ОО77', 'С-ОО77', 'С-АС77', 'М-ММ77']
# x.close()




# 4 секции, каждая представляет число до 255.
# после может быть\а может и не быть порт - числом от 0 до 65535.
# необходимо найти все валидные айпи
#
# gjhdrfegfrewdvgf
# 45.7.111.54:8553
# fojghofsdvdgfv
# 66.33.77.12
# 223.12.102.43:47856
# 44.78.12.776
# 4.212.1.124:27341
# 32.5.34.22:32
# 111.232.65.2:735
# 77.11.22.66:1
# 5.34.21.75:99999


# ipii = re.findall(r'(r'\d|\d\d|1\d\d|2[0-4]\d|25[0-5].\d|\d\d|1\d\d|2[0-4]\d|25[0-5].\d|\d\d|1\d\d|2[0-4]\d|25[0-5].\d|\d\d|1\d\d|2[0-4]\d|25[0-5].', y)

# print('адреса = ', ipii)

x.close()