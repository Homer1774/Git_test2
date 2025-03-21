# Создание словаря
a = {}
b = {'a': 1, 'b': 2}
c = dict(qwe = 'asd', zxc= 1)
d = dict([(1, 1), (2, 2)])
e = dict.fromkeys(['a', 'b'])  # {'a': None, 'b': None}
f = dict.fromkeys(['a', 'b'], 100) # {'a': 100, 'b': 100}
g = {a: a for a in range(3)} # {0: 0, 1: 1, 2: 2}

# Методы

b1 = b.copy()
print(b.get('a')) #Возвращает значение ключа
print(b.items())
print(b.keys())

b['3'] = 65
print(b.pop('3'))

print(b.setdefault('a')) # Возвращает значение по ключу или добавляет ключ со значением по умолчанию, если ключ отсутствует
b.update([('qwe', 321)])
print(b.values())

my_dict = {}
my_dict.update({'another_key': 'another_value'})  # Дополняем.
my_dict.update({'another_key': 'yet_another_value'})  # Обновляем.
print(my_dict)

print(b)