def stepen(a,b):#Функция
    if b < 0:#Проверка положительности числа
        b=abs(b)#модуль числа
    for i in range(b):# цикл до числа b
            a *=a #Возведение в степень
            return a

a = int(input('Введите a '))
b = int(input('Введите b '))
print(stepen(a, b))