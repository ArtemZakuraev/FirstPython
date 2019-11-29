def del_itel(arg1, arg2)#Функция
    try: # Попытка если удачно выполняем деление
        result = arg1/arg2
        return int(result)
    except ZeroDivisionError: #исключение
           print('На ноль делить нелья')

perv = int(input('Введите первое число '))
vtor = int(input('Введите второе число '))
print(del_itel(perv, vtor))
