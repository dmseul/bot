# -*- coding: utf8 -*-
import random
from vk_api import VkUpload
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import requests
import sqlite3 as sql

session = requests.Session()

vk = vk_api.VkApi(token='30c34278ed19e41caf63623a32bea086a253d77d45a5e9508485ad4ae41e5ef4482f876fcbd0e2bd035d1')

attachments = []

upload = VkUpload(vk)
image_url = 'https://images-na.ssl-images-amazon.com/images/I/61%2Bh1sZqpTL._SY355_.png'
image_url2 = 'https://cs.pikabu.ru/post_img/2013/06/25/6/1372148148_386219844.jpg'
image_url3 = 'https://pp.userapi.com/c831109/v831109497/115051/gdWtlHMsRDg.jpg'
image = session.get(image_url, stream=True)
image2 = session.get(image_url2, stream=True)
image3 = session.get(image_url3, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
photo2 = upload.photo_messages(photos=image2.raw)[0]
photo3 = upload.photo_messages(photos=image3.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)
attachments.append(
    'photo{}_{}'.format(photo2['owner_id'], photo2['id'])
)
attachments.append(
    'photo{}_{}'.format(photo3['owner_id'], photo3['id'])
)

demki = ['audio186841206_456240001', 'audio186841206_456240005', 'audio186841206_456240003', 'audio186841206_456240002',
         'audio186841206_456240000']

songs = ['audio186841206_456239904', 'audio186841206_456240004', 'audio186841206_456239981', 'audio186841206_456239980',
         'audio186841206_456239966', 'audio186841206_456239947', 'audio186841206_456239924', 'audio186841206_456240006',
         'audio186841206_456239995', 'audio186841206_456239927', 'audio186841206_456239895', 'audio186841206_456239849',
         'audio186841206_456239818']

print('Server started')

longpoll = VkBotLongPoll(vk, 183732788)

vk2 = vk.get_api()
zk = False
dl = False


def zvanie_2(peer_id, from_id):
    connection = sql.connect('user.sqlite', check_same_thread=False)
    q = connection.cursor()
    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (from_id))
    result = q.fetchall()
    if len(result) == 0:
        vk2.messages.send(
            random_id=0,
            peer_id=peer_id,
            message='Сначала создайте аккаунт!'
        )
    else:
        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (from_id))
        result = q.fetchall()
        balance = result[0][3]
        zvanie = result[0][5]
        zv1 = 'Бомж'
        zv2 = 'Бизнесмен'
        zv3 = 'Миллионер'
        zv4 = 'Миллиардер'
        zv5 = 'Путин'
        if zvanie != 10:
            if balance < 100000:
                if zvanie == 0:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        0,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv1
                    )
            if 100000 <= balance < 1000000:
                if zvanie == 1:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        1,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv2
                    )
            if 1000000 <= balance < 1000000000:
                if zvanie == 2:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        2,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv3
                    )
            if 1000000000 <= balance < 1000000000000:
                if zvanie == 3:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        3,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv4
                    )
            if balance >= 1000000000000:
                if zvanie == 4:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        4,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv5
                    )



try:
    for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.MESSAGE_NEW:
                if True:
                    if 'прив' in event.object.text.lower() or event.object.text.lower() == 'здарова' or 'салам' in event.object.text.lower() or event.object.text.lower() == 'начать':
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Саламалейкум всем')
                        time.sleep(1)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='''Напиши "Функции", чтобы я скинул список моих функций''')
                    elif event.object.text.lower() == 'функции':
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='''Cписок функций ниже:\n\n'"песня" - скинуть случайную песню\n\n"демка" - скинуть случайную демку🤤\n\n"создать аккаунт" - создать игровой аккаунт\n\n"игры" - посмотреть игрововые функции\n\n"баг [описание проблемы]" - сообщить о проблеме\n\n\n\n\n\ncreated by @dmseul'''
                        )
                    elif 'баг' in event.object.text.lower():
                        bag = event.object.text.lower().split("баг")[-1]
                        vk2.messages.send(
                            random_id=0,
                            peer_id=186841206,
                            message='Найдена проблема!\n' + '"' + bag + '"\n'
                        )
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Создателю сообщено о баге, спасибо за внимательность.'
                        )
                    elif event.object.text.lower() == 'игры':
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            connection = sql.connect("user.sqlite", check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            print(result)
                            user_name = result[0][1]
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message=user_name + """, мои игровые функции:\n\n"Профиль"\n\n"Звания" - посмотреть информацию о существующих званиях\n\n'"Баланс" - зачисление на баланс 10$, если у вас меньше 10$\n\n"Кубик [грань(от 1 до 6)]" - стоимость игры 100$\n\n"Казино [ставка]"\n\n"Собственность [id]":\n
Дом - 1(1000000$)
Машина - 2(100000$)
Бар - 3(1000000000$)"""
                        )
                    elif 'дай миллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай миллион ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 1000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Миллион зачислен игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери миллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери миллион ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 1000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Миллион вычтен у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'дай тысячу' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай тысячу ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 1000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Тысяча зачислена игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери тысячу' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери тысячу ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 1000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Тысяча вычтена у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )

                    elif event.object.text.lower() == 'создать аккаунт':
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            user_info = vk.method("users.get",
                                                  {"user_ids": event.object.from_id, "fields": "first_name"})
                            user_name = user_info[0]["first_name"]
                            print("Добавлен участник")
                            q.execute(
                                "INSERT INTO user_inform1 (Name, User_ID, Balance, Zvanie) VALUES ('%s', '%s', '%s', '%s')" % (
                                user_name,
                                event.object.from_id,
                                0, 0))
                            connection.commit()
                            connection.close()
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Аккаунт успешно создан'
                            )
                        else:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Аккаунт уже создан.\nНапишите "Профиль", чтобы его просмотреть'
                            )
                    elif event.object.text.lower() == 'звания':
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Звания:\n\n"Бомж" - начальное звание\n\n"Бизнесмен" - нужно иметь больше ста тысячь на счету\n\n"Миллионер" - нужно иметь больше миллиона на счету\n\n"Миллиардер" - нужно иметь больше миллиарда на счету\n\n"Путин" - нужно иметь больше триллиона на счету'
                        )

                    elif event.object.text.lower() == 'профиль':
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            print(result)
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            user_id = result[0][0]
                            name = result[0][1]
                            balance = result[0][3]
                            ownment = result[0][4]
                            zvanie = result[0][5]

                            ownment_message = ""
                            if zvanie == 0:
                                zvanie = 'Бомж'
                            elif zvanie == 1:
                                zvanie = 'Бизнесмен'
                            elif zvanie == 2:
                                zvanie = 'Миллионер'
                            elif zvanie == 3:
                                zvanie = 'Миллиардер'
                            elif zvanie == 4:
                                zvanie = 'Путин'
                            elif zvanie == 10:
                                zvanie = 'Админ'

                            if ownment != None:
                                dom = 0
                                car = 0
                                bar = 0
                                ownment = ownment.split(",")
                                ownment = ownment[:-1]
                                for own in ownment:
                                    if int(own) == 1:
                                        dom += 1
                                    elif int(own) == 2:
                                        car += 1
                                    elif int(own) == 3:
                                        bar += 1
                                ownment_message = "Машины: " + str(car) + "\nДома: " + str(dom) + "\nБары: " + str(bar)
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message="ID: " + str(user_id) + "\nВаше имя: " + str(
                                    name) + "\n💰Баланс: " + str(
                                    balance) + "$" + '\nЗвание: ' + zvanie + "\nВаши владения:\n" + ownment_message

                            )
                    elif zk == True:
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            balance = result[0][3]
                            try:
                                stav = int(event.object.text.lower().split("дуэль ")[-1])
                            except:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Введите корректную сумму ставки'
                                )
                                continue
                            if stav > 0:
                                if dl == False:
                                    if stav <= balance:
                                        duelant = event.object.from_id
                                        stavka = stav
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Ждём, пока кто-то примет дуэль'
                                        )
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance - stavka,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        dl = True
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств!'
                                        )
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Кто-то уже начал дуэль!\nНапишите "дуэль принять", чтобы принять её'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Ставка должна быть больше нуля!'
                                )

                    elif zk == True:
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if dl == True:
                                if event.object.from_id != duelant:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    balance = result[0][3]
                                    name = result[0][1]
                                    if balance >= stavka:
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                        balance - stavka, event.object.from_id))
                                        dl_rs = random.randint(1, 2)
                                        dl_vi = 2 * stavka
                                        connection.commit()
                                        connection.close()
                                        if dl_rs == 1:
                                            connection = sql.connect('user.sqlite', check_same_thread=False)
                                            q = connection.cursor()
                                            q.execute(
                                                "SELECT * FROM user_inform1 WHERE User_ID = %s" % (
                                                    event.object.from_id))
                                            result = q.fetchall()
                                            balance = result[0][3]
                                            name = result[0][1]
                                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                balance + dl_vi, event.object.from_id))
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message=name + ', поздравляю с победой!\nВаш выигрыш:' + str(
                                                    dl_vi) + '$'
                                            )
                                            connection.commit()
                                            connection.close()
                                            dl = False
                                        if dl_rs == 2:
                                            connection = sql.connect('user.sqlite', check_same_thread=False)
                                            q = connection.cursor()
                                            q.execute(
                                                "SELECT * FROM user_inform1 WHERE User_ID = %s" % (duelant))
                                            result = q.fetchall()
                                            balance = result[0][3]
                                            name = result[0][1]
                                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                balance + dl_vi, duelant))
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message=name + ', поздравляю с победой!\nВаш выигрыш:' + str(
                                                    dl_vi) + '$'
                                            )
                                            connection.commit()
                                            connection.close()
                                            dl = False
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств, чтобы принять дуэль:(')
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Нельзя принять дуэль от самого себя!!!')
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Дуэль пока что никто не начал')
                    elif zk == True:
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (duelant))
                            result = q.fetchall()
                            balance = result[0][3]
                            name = result[0][1]
                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                balance + stavka, duelant))
                            connection.commit()
                            connection.close()
                            stav = 0
                            dl = False
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Дуэль успешно отменена')
                    elif 'собственность' in event.object.text.lower():
                        try:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            if len(result) == 0:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Сначала создайте аккаунт!'
                                )
                            else:
                                realty = int(event.object.text.lower().split("собственность")[1])
                                if realty == 1:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    ownment = result[0][4]
                                    if money >= 1000000:
                                        if ownment != None:
                                            q.execute("UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                str(ownment) + "1,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили дом!'
                                            )
                                        else:
                                            q.execute(
                                                "UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                    "1,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили дом!'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств для покупки!'
                                        )
                                elif realty == 2:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    ownment = result[0][4]
                                    if money >= 100000:
                                        if ownment != None:
                                            q.execute("UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                str(ownment) + "2,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 100000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили машину!'
                                            )
                                        else:
                                            q.execute(
                                                "UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                    "2,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 100000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили машину!!'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств для покупки!'
                                        )
                                elif realty == 3:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    ownment = result[0][4]
                                    if money >= 1000000000:
                                        if ownment != None:
                                            q.execute("UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                str(ownment) + "3,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили бар!'
                                            )
                                        else:
                                            q.execute(
                                                "UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                    "3,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили бар!'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств для покупки!'
                                        )
                        except:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message="Введите корректный id покупки!"
                            )
                    elif "баланс" in event.object.text.lower():
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            balance2 = result[0][3]
                            if balance2 < 10:
                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                q = connection.cursor()
                                q.execute(
                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (int(balance2) + 10,
                                                                                                     event.object.from_id))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Вам зачислено 10$!\nБаланс: " + str(balance2 + 10)
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Нужно иметь меньше 10$ на балансе!"
                                )
                    elif "казино" in event.object.text.lower():
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )

                        else:
                            try:
                                money = result[0][3]
                                kazino = random.randint(1, 2)
                                rate = int(event.object.text.lower().split("казино ")[-1])
                                if rate > 0:
                                    if result[0][3] >= rate:
                                        q.execute(
                                            "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                int(money) -
                                                rate,
                                                event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        if kazino == 1:
                                            coefficient = random.randint(1, 4)
                                            if coefficient == 1:
                                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute(
                                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                        int(money) +
                                                        rate * 2,
                                                        event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    message="Вы выиграли " + str(rate * 2) + "!"
                                                )
                                                zvanie_2(event.object.peer_id, event.object.from_id)
                                            elif coefficient == 2:
                                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute(
                                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                        int(money) +
                                                        rate * 3,
                                                        event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    message="Вы выиграли " + str(rate * 3) + "!"
                                                )
                                                zvanie_2(event.object.peer_id, event.object.from_id)
                                            elif coefficient == 4:
                                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute(
                                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                        int(money) +
                                                        rate * 4,
                                                        event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    message="Вы выиграли " + str(rate * 4) + "!"
                                                )
                                                zvanie_2(event.object.peer_id, event.object.from_id)
                                            else:
                                                x7 = random.randint(1, 2)
                                                if x7 == 1:
                                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                                    q = connection.cursor()
                                                    q.execute(
                                                        "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                            int(money) +
                                                            rate * 7,
                                                            event.object.from_id))
                                                    connection.commit()
                                                    connection.close()
                                                    vk2.messages.send(
                                                        random_id=0,
                                                        peer_id=event.object.peer_id,
                                                        message="Вы выиграли " + str(rate * 7) + "!"
                                                    )
                                                    zvanie_2(event.object.peer_id, event.object.from_id)
                                                else:
                                                    vk2.messages.send(
                                                        random_id=0,
                                                        peer_id=event.object.peer_id,
                                                        message="Вы проиграли " + str(rate) + ":("
                                                    )
                                                    zvanie_2(event.object.peer_id, event.object.from_id)
                                        elif kazino == 2:
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message="Вы проиграли " + str(rate) + ":("
                                            )
                                            zvanie_2(event.object.peer_id, event.object.from_id)
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message="Недостаточно средств!"
                                        )
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message="Cтавка должна быть больше нуля!"
                                    )
                            except:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Введите корректную сумму ставки!"
                                )
                    elif 'кубик' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            try:
                                if balance >= 100:
                                    cube = random.randint(1, 6)
                                    user_cube = int(event.object.text.lower()[-1])
                                    user_win = random.randint(1000, 10000)
                                    balance = result[0][3]
                                    q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                        balance - 100, event.object.from_id))
                                    connection.commit()
                                    connection.close()
                                    user_name = result[0][1]
                                    if user_cube == cube:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute(
                                            "SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                        result = q.fetchall()
                                        balance = result[0][3]
                                        user_name = result[0][1]

                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                        balance + user_win, event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message=user_name + ", вы угадали! 😯 Выйгрыш " + str(user_win) + "$"
                                        )
                                        zvanie_2(event.object.peer_id, event.object.from_id)
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message=user_name + ", вы проиграли! Выпало число " + str(cube) + " 😔"
                                        )
                                        zvanie_2(event.object.peer_id, event.object.from_id)
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message="Недостаточно средств"
                                    )
                            except:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Введите корректную сторону кубика"
                                )
                    elif event.object.text.lower() == 'демка':
                        message2 = random.randint(0, 4)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=demki[message2],
                            message='👌🏻👈🏻'
                        )
                    elif 'бит' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=attachments[0],
                            message='блинб биты'
                        )
                    elif 'аниме' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=attachments[1],
                            message=' '
                        )
                    elif event.object.text.lower() == 'песня':
                        number = random.randint(0, 13)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=songs[number]
                        )
                    elif 'прон' in event.object.text.lower() or 'порн' in event.object.text.lower() or 'дота' in event.object.text.lower() or 'dota' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=attachments[2],
                            message='Любишь гей порно я смотрю?'
                        )
                    elif 'как дела' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Норм, нога только чешется')
                    elif 'ты пидор' in event.object.text.lower() or 'ты педик' in event.object.text.lower() or 'ты гандон' in event.object.text.lower() or 'ты мудак' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='За базар вывезешь?')
        except:
            time.sleep(1)
except:
    time.sleep(60)
