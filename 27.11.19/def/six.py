def int_func(text):# Функция принимает строку
    print(text.title()) # Печатаем 1 элемент строки большими остальное маленькими

text = input('Введите строку ') # Ввод строки
text2 = text.split() # Сплитим введенную строку
for i in text2: # Для элемента спличеной строки
    int_func(i) #Передать в функцию

