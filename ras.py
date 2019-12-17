# -*- coding: windows-1251 -*-
# Пробовал с апи телеграма но у нас в россии он заблокирован, сам клиент проде обходил блок а апи не может
# Импортирую
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import creds.json # Импортирую файл с ключем API




CREDENTIALS_FILE = 'creds.json'  # файл с ключами апи для вконтакта

#dday = datetime.datetime.today().strftime("%m/%d/%Y") # тут я собирал дату текущую для логов (добавлю логирование действий кто и когда что сделал, писать буду в таблицы гугл через апи
#print (dday)


def write_msg(user_id, message, random_id): #  функция ответа в чат контакта
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

# API
token = creds.json.spreadsheet_id # берем ключик из апи файла (ну свой ключик я выкладывать уж не буду

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# сами сообщения генерируют метод
longpoll = VkLongPoll(vk)



for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # если ответ
            if request == "привет":


                klaster = '4245' # задаю кластер 1с руками так как поднял один ras сервер


                # Сообщение от ras

                os.chdir('C:/Program Files/1cv8/8.3.10.2699/bin') # меняю директорию на ту где установлена платформа 1с
                command = 'rac.exe msc-zvg-1c-01v:' + klaster +  ' cluster list' # генерим комманду
                pipe = os.popen(command) # исполняем
                result = pipe.read() # сохраняем результат
                result = result.encode('cp1251').decode('cp866')# декодирую, так как у 1с иная русскоязычная кодировка
                write_msg(event.user_id, result, '') # пишу в чат
                write_msg(event.user_id, 'Выберите действие', '')# пишу в чат
                write_msg(event.user_id, '1   Посмотреть базы на сервере ' + klaster, '')# пишу в чат
                 # sheet_d(event.user_id, result, dday)# отключил пока логирование
                for event in longpoll.listen():

                    # Если пришло новое сообщение
                    if event.type == VkEventType.MESSAGE_NEW:

                        # Если оно имеет метку для меня( то есть бота)
                        if event.to_me:

                            # Сообщение от пользователя
                            request = event.text



                            # если ответ
                            if request == "1":
                                os.chdir('C:/Program Files/1cv8/8.3.10.2699/bin')# тут все как блком выше
                                command = 'rac msc-zvg-1c-01v:4245 infobase --cluster=82effbca-f283-4685-b596-0af337ebbfbb summary list'
                                pipe = os.popen(command)
                                result = pipe.read()
                                result = result.encode('cp1251').decode('cp866')
                                my_list = result.split('\n\n') # так как я не получаю словарь а строку начинаем муторную процедуру разбора
                                # так как мне нужно из разных мест получить и слить данные, хочу забирать в словарь название базы и ее guid а они в разных списках получаються
                                my_dict = {}# итоговый словарь
                                vr_dict = {}# временный словарь
                                otvet_dict = {}# временный словарь 2

                                for en in my_list:# еще раз разбираем строку по сплиту
                                    en = en.split('\n')
                                    i=0
                                    for enu in en:# и еще раз
                                        i+=1
                                        enu = enu.split(':')

                                        try:
                                            vr_dict.update({enu[0]:enu[1]})# вот тут отсекать будем коментарии из службы 1с
                                        except IndexError:
                                            break
                                        if i==3:# проверка, что не выполнили больше 2 подходов
                                            name = vr_dict.get('name     ')# получаю имя базы
                                            infobase = vr_dict.get('infobase ') # получаю guid
                                            my_dict.update({name: infobase})# собираю итоговый словарь

                                    # with open('D:/bot/otvet.txt', 'w+') as otvet: # использовал для дебага, так как контакт блочит вывод массива в цикле как флуд
                                # с флудом проблемма, у контакта длинна сообщения ограничина приходиться в цикле словарь печатать если более 25 баз будет бан за флуд на 5 мин
                                for index, item in enumerate(my_dict):# выбор номера базы, чтобы не перебивать имя

                                    otvet_dict.update({index+1:item})# словарь временный 2 создаем для ответов пользователя по базам
                                    stroka = 'Номер '+ str(index+1) + ' База ' + item
                                    #print(stroka) # тут я печатал в консоль за место чата обходил флуд на этапе разработки




                                write_msg(event.user_id, 'Выберите номер базы ', '')# ответ от пользователя

                                for event in longpoll.listen():

                                    # Если пришло новое сообщение
                                    if event.type == VkEventType.MESSAGE_NEW:

                                        # Если оно имеет метку для меня( то есть бота)
                                        if event.to_me:

                                            # Сообщение от пользователя #тут уже выше было описание этого блока
                                            request = event.text
                                            request = int(request)
                                            base = otvet_dict.get(request)
                                            otvet = my_dict.get(base)
                                            otvet = otvet.split(' ')
                                            print(otvet[1])
                                            write_msg(event.user_id, 'Список соединений базы  '+ base, '')
                                            os.chdir('C:/Program Files/1cv8/8.3.10.2699/bin')
                                            command = 'rac msc-zvg-1c-01v:4245 connection --cluster=82effbca-f283-4685-b596-0af337ebbfbb list --infobase='+otvet[1]
                                            pipe = os.popen(command)
                                            result = pipe.read()
                                            result = result.encode('cp1251').decode('cp866')
                                            try:
                                                write_msg(event.user_id, result, '')
                                            except vk_api.exceptions.ApiError:
                                                write_msg(event.user_id, 'Список соединений пуст ', '')
                                                break



            elif request == "shutdown": # загасить бота
                write_msg(event.user_id, "Пока((", '')
                exit()



            else:# если поступило сообщение непонятное
                write_msg(event.user_id, "ЧТА ? ", '')
