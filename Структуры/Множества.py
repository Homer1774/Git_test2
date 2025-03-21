a = set()
b = set('hello')
c = {'a', 'b', 'c'}
d = {i + 1 for i in range(10)}

hello = {'hello', 'world', 'Dayan'}
hello1 = {'hello', 'world', 'hello', 'Dayan'}
print(len(hello1))
print(hello.isdisjoint(hello1))
print(hello == hello1)

#set.issubset(other) или set <= other  #все элементы set принадлежат other
# set.union(other, ...) или set | other | ...     #объединение нескольких множеств
# set.intersection(other, ...) или set & other & ...   #пересечение
# set.difference(other, ...) или set - other - ...    #множество из всех элементов set, не принадлежащие ни одному из other
# set.symmetric_difference(other); set ^ other    #множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих
# set.copy()   #копия множества

print(hello1 | hello)