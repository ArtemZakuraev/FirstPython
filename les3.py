"""
Добавляем комментарий
"""
string = input('введите число\n ')
# Собираем из строки число
number = int(string)
number1 = int(string+string)
number2= int(string+string+string)
# проверяем промежуточный итог
print(number)
print(number1)
print(number2)
# сама операция
itog = (number + number1 + number2)
print(itog)