number = int(input('введите кол-во секунд\n '))
minute = number/60
Hour = minute/60 #or Hour = (number/60)/60

print('Часов ',Hour,'Минут ',minute) # or
print(f"Часов {Hour} Минут {minute}")