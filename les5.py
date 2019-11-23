viruchka = int(input('введите cумму выручки\n'))
izderzhki = int(input('введите cумму издержек\n'))

if viruchka > izderzhki:
    rezult = (viruchka / izderzhki)*100
    print('Отлично вы в плюсе',rezult, '%')
else:
    rezult = (izderzhki / viruchka) * 100
    print('Плохо вы в минусе', rezult, '%')