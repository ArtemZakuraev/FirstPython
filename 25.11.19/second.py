spisok = [str(i) for i in input('Введите содержимое списка через пробел:').split()] # Наполняем списко в консоли

i=0
spisok2 = list() #Задаю пустой список
if len(spisok) %2 == 0: #Проверяем четность длинны

    for i in range(i, len(spisok), 2):# четный значит по всей динне работаем


           spisok2.append(spisok[i+1])# наполняем
           spisok2.append(spisok[i])
else:

    for i in range(i, len(spisok)-1, 2):# не четный работаем -1 длинну


        spisok2.append(spisok[i + 1])# наполняем
        spisok2.append(spisok[i])

    spisok2.append(spisok[-1])# докидываем -1 элеммент
print(spisok2)# выводим результат
