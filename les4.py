srtoka = input('введите число\n')
#счетчик цикла!
i = 0
#если разбираем по элементам строку то больше не будет
min = 9

while i < len(srtoka):

    if min > int(srtoka[i]):
         min = int(srtoka[i])
    i+=1
print(min)


