# -*- coding: windows-1251 -*-
# �������� � ��� ��������� �� � ��� � ������ �� ������������, ��� ������ ����� ������� ���� � ��� �� �����
# ����������
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import creds.json # ���������� ���� � ������ API




CREDENTIALS_FILE = 'creds.json'  # ���� � ������� ��� ��� ���������

#dday = datetime.datetime.today().strftime("%m/%d/%Y") # ��� � ������� ���� ������� ��� ����� (������� ����������� �������� ��� � ����� ��� ������, ������ ���� � ������� ���� ����� ���
#print (dday)


def write_msg(user_id, message, random_id): #  ������� ������ � ��� ��������
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

# API
token = creds.json.spreadsheet_id # ����� ������ �� ��� ����� (�� ���� ������ � ����������� �� �� ����

# ������������ ��� ����������
vk = vk_api.VkApi(token=token)

# ���� ��������� ���������� �����
longpoll = VkLongPoll(vk)



for event in longpoll.listen():

    # ���� ������ ����� ���������
    if event.type == VkEventType.MESSAGE_NEW:

        # ���� ��� ����� ����� ��� ����( �� ���� ����)
        if event.to_me:

            # ��������� �� ������������
            request = event.text

            # ���� �����
            if request == "������":


                klaster = '4245' # ����� ������� 1� ������ ��� ��� ������ ���� ras ������


                # ��������� �� ras

                os.chdir('C:/Program Files/1cv8/8.3.10.2699/bin') # ����� ���������� �� �� ��� ����������� ��������� 1�
                command = 'rac.exe msc-zvg-1c-01v:' + klaster +  ' cluster list' # ������� ��������
                pipe = os.popen(command) # ���������
                result = pipe.read() # ��������� ���������
                result = result.encode('cp1251').decode('cp866')# ���������, ��� ��� � 1� ���� ������������� ���������
                write_msg(event.user_id, result, '') # ���� � ���
                write_msg(event.user_id, '�������� ��������', '')# ���� � ���
                write_msg(event.user_id, '1   ���������� ���� �� ������� ' + klaster, '')# ���� � ���
                 # sheet_d(event.user_id, result, dday)# �������� ���� �����������
                for event in longpoll.listen():

                    # ���� ������ ����� ���������
                    if event.type == VkEventType.MESSAGE_NEW:

                        # ���� ��� ����� ����� ��� ����( �� ���� ����)
                        if event.to_me:

                            # ��������� �� ������������
                            request = event.text



                            # ���� �����
                            if request == "1":
                                os.chdir('C:/Program Files/1cv8/8.3.10.2699/bin')# ��� ��� ��� ����� ����
                                command = 'rac msc-zvg-1c-01v:4245 infobase --cluster=82effbca-f283-4685-b596-0af337ebbfbb summary list'
                                pipe = os.popen(command)
                                result = pipe.read()
                                result = result.encode('cp1251').decode('cp866')
                                my_list = result.split('\n\n') # ��� ��� � �� ������� ������� � ������ �������� �������� ��������� �������
                                # ��� ��� ��� ����� �� ������ ���� �������� � ����� ������, ���� �������� � ������� �������� ���� � �� guid � ��� � ������ ������� �����������
                                my_dict = {}# �������� �������
                                vr_dict = {}# ��������� �������
                                otvet_dict = {}# ��������� ������� 2

                                for en in my_list:# ��� ��� ��������� ������ �� ������
                                    en = en.split('\n')
                                    i=0
                                    for enu in en:# � ��� ���
                                        i+=1
                                        enu = enu.split(':')

                                        try:
                                            vr_dict.update({enu[0]:enu[1]})# ��� ��� �������� ����� ���������� �� ������ 1�
                                        except IndexError:
                                            break
                                        if i==3:# ��������, ��� �� ��������� ������ 2 ��������
                                            name = vr_dict.get('name     ')# ������� ��� ����
                                            infobase = vr_dict.get('infobase ') # ������� guid
                                            my_dict.update({name: infobase})# ������� �������� �������

                                    # with open('D:/bot/otvet.txt', 'w+') as otvet: # ����������� ��� ������, ��� ��� ������� ������ ����� ������� � ����� ��� ����
                                # � ������ ���������, � �������� ������ ��������� ���������� ����������� � ����� ������� �������� ���� ����� 25 ��� ����� ��� �� ���� �� 5 ���
                                for index, item in enumerate(my_dict):# ����� ������ ����, ����� �� ���������� ���

                                    otvet_dict.update({index+1:item})# ������� ��������� 2 ������� ��� ������� ������������ �� �����
                                    stroka = '����� '+ str(index+1) + ' ���� ' + item
                                    #print(stroka) # ��� � ������� � ������� �� ����� ���� ������� ���� �� ����� ����������




                                write_msg(event.user_id, '�������� ����� ���� ', '')# ����� �� ������������

                                for event in longpoll.listen():

                                    # ���� ������ ����� ���������
                                    if event.type == VkEventType.MESSAGE_NEW:

                                        # ���� ��� ����� ����� ��� ����( �� ���� ����)
                                        if event.to_me:

                                            # ��������� �� ������������ #��� ��� ���� ���� �������� ����� �����
                                            request = event.text
                                            request = int(request)
                                            base = otvet_dict.get(request)
                                            otvet = my_dict.get(base)
                                            otvet = otvet.split(' ')
                                            print(otvet[1])
                                            write_msg(event.user_id, '������ ���������� ����  '+ base, '')
                                            os.chdir('C:/Program Files/1cv8/8.3.10.2699/bin')
                                            command = 'rac msc-zvg-1c-01v:4245 connection --cluster=82effbca-f283-4685-b596-0af337ebbfbb list --infobase='+otvet[1]
                                            pipe = os.popen(command)
                                            result = pipe.read()
                                            result = result.encode('cp1251').decode('cp866')
                                            try:
                                                write_msg(event.user_id, result, '')
                                            except vk_api.exceptions.ApiError:
                                                write_msg(event.user_id, '������ ���������� ���� ', '')
                                                break



            elif request == "shutdown": # �������� ����
                write_msg(event.user_id, "����((", '')
                exit()



            else:# ���� ��������� ��������� ����������
                write_msg(event.user_id, "��� ? ", '')
