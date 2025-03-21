try: 
    # file = open("Раб файлы/my_text.txt", encoding='utf-8') 
    with open("Раб файлы/my_text.txt", encoding='utf-8') as file:
        s = file.readlines()
        print(s)
    # try:
    #     s = file.readlines()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print("Файл не найден или его не возможно открыть")
except:
    print("Ошибка")
finally:
    print(file.closed)
