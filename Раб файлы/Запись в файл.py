import pickle

books = [
    ("Eвгений", "Пушкин", 200),
    ("Александр", "Сушкин", 340),
    ("Гений", "Пукин", 20),
]

file = open("Раб файлы/my_bin.bin", "rb")
bs = pickle.load(file)
file.close()
print(bs)