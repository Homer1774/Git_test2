# Удаление дубликатов
# q = [1, 2, 2, 3, 4, 4, 5]
# a = list(set(q))
# print(a)


# Сортировка по первой букве и в алф порядке
# q = ["apple", "banana", "avocado", "grape", "apricot"]
# def sort(x):
#     a = []
#     for i in x:
#         if (i.lower()).startswith('a'):
#             a.append(i)
#     return sorted(a) 
# print(sort(q))


#Сумма квадратов положительных чисел
# q = [-1, 2, 3, -4, 5]
# def summa(x):
#     a = 0
#     for i in x:
#         if i > 0:
#             a += i ** 2
#     return a
# print(summa(q))


# Перевернуть строки
# a = ["hello", "world"]
# def reverse(x):
#     b = []
#     for i in x:
#         b.append(i[::-1])
#     x = b
#     return x
# print(reverse(a))


# Словарь частоты
# q = ["apple", "banana", "apple", "orange", "banana", "banana"]
# def qwer(x):
#     a = {i: x.count(str(i)) for i in x}
#     sorted(a.keys())
#     sorted(a.items())
#     return a
# print(qwer(q))


# Смешивание списков
# q = [1, 2, 3] 
# w = ['a', 'b', 'c']
# def a(x, z):
#     b = [i for f in zip(x, z) for i in f]
#     return b
# print(a(q, w))



# def compress(lst):
#     if not lst:
#         return []
#     compressed = [lst[0]]
#     for item in lst[1:]:
#         if item != compressed[-1]:
#             compressed.append(item)
#     return compressed

# print(compress([1, 1, 2, 2, 3, 1, 1]))  


# spisok = ['Dayan', 'Aidar', 'Aleksandr', 'Anna']
# def all_eq(lst):
#     value = [len(i) for i in lst]
#     max_value = max(value)
#     new_spisok = []
#     for s in range(len(lst)):
#         while len(lst[s]) < max_value:
#             lst[s] += '_'
#     new_spisok.append(lst[s]) 
#     lst = new_spisok

# all_eq(spisok)
# print(spisok)
# spisok.





