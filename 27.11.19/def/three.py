""""
Я наверное индус но цикл не охото тут делать
"""
def my_func(arg1, arg2, arg3): #Функция
    li = [arg1, arg2, arg3] #Собираем список из аргументов
    first_max = max(li) #Находим 1 максимум
    li.remove(first_max)#Удаляем 1 максимум из списка
    second_max = max(li)#Находим 2 максимум
    result = first_max + second_max #Складываем


    print(result)

a = int(input('Введите 1 элемент ')) #Ввод элементов
b = int(input('Введите 2 элемент '))
c = int(input('Введите 3 элемент '))
my_func(a, b, c) #Вызов функции