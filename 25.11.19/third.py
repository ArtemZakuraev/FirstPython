stroka = input('Введите строку ') #Получаем строку
ne_stroka = (stroka.split()) #Сплитим строку по пробелам


for st in ne_stroka: # Для st из ne_stroka цикл
    if len(st) > 10: #если длинна st больше 10 тогда
        print(st[:10]) # печатаем с начала по 10 элемент
    else: # Иначе печатаем все
        print(st)