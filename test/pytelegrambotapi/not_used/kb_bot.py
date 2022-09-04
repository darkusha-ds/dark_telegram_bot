from datetime import time, date, datetime # библиотека позволяющая смотреть время
import telebot as tg# библиотека для самого бота в телеграмме
import sysconfig
import sys
import math
import types
import config
class event:
    def __init__(self, text, begin_h, begin_m, all_event): # класс для определения времени
        self.text = text # просто объявляем их
        self.begin_h = begin_h
        self.begin_m = begin_m
        self.all_event = all_event

class user:
    def __init__(self, name, id, kb):
        self.name = name # класс для регистрации, который будет хранить ник, id и группу
        self.id = id
        self.kb = kb

users = []
arr = []
arr.append(event("Подъём - 8:00", 8, 0, 0))
arr.append(event("В 8:30 Зарядка!!!", 8, 30, 0))
arr.append(event("Завтрак у нас в 9:00", 9, 0, 0))
arr.append(event("В 9:30 начало образовательной программы", 9, 30, 1))
arr.append(event("С 11:00 до 11:15 у нас коротенький перекус", 11, 0, 0))
arr.append(event("Продолжение образовательной программы начинается в 11:30", 11, 30, 1))
arr.append(event("В 13:00 начинается самостоятельная работа над проектами", 13, 0, 0))
arr.append(event("В 2 часа ( или 14:00, как хотите ) у нас обед.", 14, 0, 0))
arr.append(event("С 15:00 до 16:00 у нас как обычно тихий час, почти как в детском садике :D", 15, 0, 0))
arr.append(event("Полдник в 16:00 ", 16, 0, 0))
arr.append(event("16:30 - последние занятия ", 16, 30, 1))
arr.append(event("В 18:00 должна быть спортивно-развлекательная программа ( или возможно снова будут занятия :D )", 18, 0, 0))
arr.append(event("В 19:30 будет ужин",19, 0, 0))
arr.append(event("Все мероприятия запланированны на 19:30 ( ну, или конкретно спортивные часы, как хотите )", 19, 30, 0))
arr.append(event("В 21:30 поздний ужин ввиде быстрой еды, так что я бы сказала, что у тебя целых 25 минут полностью свободного времени", 21, 30, 0))
arr.append(event("В 22:00 должны все пойти спать...по идее....", 22, 0, 0))

kb1 = []
kb1.append(event("С 9:30 до 11:00 у КБ-1 Аэро в столовой.", 9, 30, 1))
kb1.append(event("С 11:30 и до 13:00 у КБ-1 Промышленный дизайн в шатре", 11, 30, 1))
kb1.append(event("С 16:30 до 18:00 у КБ-1 опять Аэро в столовой", 16, 30, 1))

kb2 = []
kb2.append(event("В 9:30 у КБ-2 будет IT в столовой до 11:00", 9, 30, 1))
kb2.append(event("С 11:30 и до 13:00 у Второго КБ в столовой Аэро", 11, 30, 1))
kb2.append(event("С 16:30 до 18:00 у КБ-2 будет  Промышленный дизайн в шатре", 16, 30, 1))

kb3 = []
kb3.append(event("У КБ-3 будет с 9:30 и до 11:00 в шатре VR/AR", 9, 30, 1))
kb3.append(event("У КБ-3 будет с 11:30 и до 13:00 в столовой IT", 11, 30, 1))
kb3.append(event("У КБ-3 будет с 16:30 и до 18:00 в столовой Аэро", 16, 30, 1))

kb4 = []
kb4.append(event("У КБ-4 с 9:30 до 11:00 в шатре Аэро", 9, 30, 1))
kb4.append(event("У КБ-4 c 11:30 до 13:00 в шатре Аэро", 9, 30, 1))
kb4.append(event("У КБ-4 с 16:30 до 18:00 в шатре Аэро", 9, 30, 1))

EGHT = '8:00 - Подъём'
HALFEGT = 'В 8:30 будет зарядка'
NINE = 'В 9:00 у нас завтрак'
HALFNIE = 'В 9:30 начинается первое занятие'
ELLEVEN = '11:00 - короткий перекус'
HALFELLEVEN = '11:30 - второе занятие'
THREETEEN = '13:00 - купаться'
FORTEEN = '14:00 - обееед'
FIVE = '15:00 - наконец-то отдых до 16:00'
FOR = 'Полдник запланирован на 16:00 '
HALFFOR = 'В 16:30 продолжаются занятия'
EGHTEEN = '18:00 у нас спортивный часок'
NINETEEN = '19:00 - Ужин'
TWENTY = '21:30 - поздний ужин'
TWELWE = '22:00 - спать, но спать кто-то врятли будет'

def check(current_id): # функция которая проверяет зарегистрирован ли человек
    for i in users:
        if i.id == current_id:
            return 1
    return 0

bot = tg.TeleBot(config.token) # тег бота необходимый для его изменения
@bot.message_handler(commands=['start']) # функция в которой проиходят все действия. commands типо данных( но я могу ошибаться), start - команда в боте для вывода следующего текста
def send_welcome(message):
    bot.reply_to(message, f'Здравствуй, я Айла, приятно с тобой познакомиться. Если нужна будет помощь по работе со мной, то просто напиши мне /help и я тебе все объясню, но сначала пройди регистрацию с помощью команды /reg')


@bot.message_handler(commands=["reg"])
def other_name(message):
    global user_id #глобальная переменная хранящая id зарегистрировшегося пользователя
    user_id = message.from_user.id # принятие информации из текста, который отправляет пользователь
    if check(user_id) == 1: #если такой id уже зарегистрирован, то не дает зарегистрироваться воторой раз
        bot.reply_to(message, f"Ошибка, ты уже прошел регистрацию")
    else:
        bot.reply_to(message, f"Пожалуйста введи свой так называемый в высшем интернете \"ник-нейм\"")

    bot.register_next_step_handler(message, get_name) # переход к следующей функции

def get_name(message):
    global name
    name = message.text.lower() #функция, которая узнает имя пользователя
    bot.reply_to(message, f"Теперь надо чтобы ты написал своё Конструкторское Бюро (проще говоря КБ)")
    bot.register_next_step_handler(message, get_kb)

def get_kb(message):
    global kb
    kb = message.text.lower() #функция, которая узнает группу
    # while not kb == 1:
    if (kb == '1') or (kb == '2') or (kb == '3') or (kb == '4'): # всего 4 кб, если ввести больше или меньше, то регистрация будет отменена и придется проходить её снова
        users.append(user(name, user_id, kb)) #добавление в конец массива user
        bot.reply_to(message, f"Ты зарегистрирован в моей базе данных. Приятного пользования")
        print(users[len(users) - 1].name)
        print(users[len(users) - 1].id) # эти 3 строки чтобы выводить в консоль информацию о зарегистрировавшихся
        print(users[len(users) - 1].kb)
    else:
        bot.reply_to(message, f"Ошибка, в нашем лагере есть от 1 до 4 Конструкторских Бюро\nРегистрация не пройдена, пройди её заново")


@bot.message_handler(commands=['help'])
def send_welcome1(message):
    cur_id = message.from_user.id
    if check(cur_id) == 1: # если данный id не зарегистрирован, то программа не даст ему выполненить дальнейшие команды
        bot.reply_to(message, f'Мои команды: \n \n' + 'all - расписание \n' + 'next - какое заняятие будет дальше \n' + "now - какое занятие сейчас \n" + "lunch - список всех обеденных перерывов" )
    else:
        bot.send_message(message.from_user.id, "Ошибка, ты не прошел регистрацию. Пожалуйста, сделай это с помощью комманды /reg")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    current_time = datetime.now().time() # переменная, котораяя будет проверять текущее время и выводить его ввиде 16 : 18 : 12 : 12312412
    s = message.text.lower() # переменная для считывания текста
    nexttime = current_time.hour
    anoter = current_time.minute
    flag = 0
    cure_id = message.from_user.id
    if check(cure_id) == 1:

        if (s =="привет") or s == "йо" or s == "здарова" or s== "привет айла":
            bot.send_message(message.chat.id, "А? Да-да, привет, " + name)
            flag = 1
        if s == "айла" or s == "эй" or s =="але":
            bot.send_message(message.from_user.id, "Да, что такое, " + name)
            flag = 1
        if s == "в каком кб я состою" :
            bot.send_message(message.from_user.id, "Насколько я помню ты состоишь в " + kb + " кб")
            flag = 1
        if s == "тварь" or s == "чмо" or s == "сука" or s == "гнида":
            bot.send_message(message.from_user.id, "Ошибка, не поняла запроса")
            flag = 1
        if s == "just a fucking machine" or s == "piece of plastic" or s == "тупой бот" or s == "кусок пластика":
            bot.send_message(message.from_user.id, "Ошибка, запроса не поняла.")
            flag = 1


        if s == "now": #какое занятие у нас сейчас
            j = 0
            for i in arr:

                eventTime = i.begin_h*100+i.begin_m
                nowTime = nexttime *100 + anoter

                if nowTime > eventTime :
                    s = i.text
                else:
                    break
                j += 1
            j -= 1
            if arr[j].all_event == 0:
                bot.send_message(message.from_user.id, s)
                print(j, "AAAAAAAAAAA")
            else:
                current_id = message.from_user.id
                current_kb = 0
                pos = 0
                for j in users:
                    if j.id == current_id:
                        current_kb = j.kb
                        break
                print(current_kb)
                if current_kb == '1':
                    if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1100:
                        bot.send_message(message.from_user.id, kb1[0].text)
                    if nexttime * 100 + anoter > 1130 and nexttime * 100 + anoter < 1300:
                        bot.send_message(message.from_user.id, kb1[1].text)
                    if nexttime * 100 + anoter > 1630 and nexttime * 100 + anoter < 1800:
                        bot.send_message(message.from_user.id, kb1[2].text)

                if current_kb == '2':
                    if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1130:
                        bot.send_message(message.from_user.id, kb2[0].text)
                    if nexttime * 100 + anoter > 1130 and nexttime * 100 + anoter < 1300:
                        bot.send_message(message.from_user.id, kb2[1].text)
                    if nexttime * 100 + anoter > 1630 and nexttime * 100 + anoter < 1800:
                        bot.send_message(message.from_user.id, kb2[2].text)
                if current_kb == '3':
                    #print("aaaaaaaaaaaaaaaaa")
                    if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1100:
                        bot.send_message(message.from_user.id, kb3[0].text)

                    if nexttime * 100 + anoter > 1130 and nexttime * 100 + anoter < 1300:
                        bot.send_message(message.from_user.id, kb3[1].text)
                    if nexttime * 100 + anoter > 1630 and nexttime * 100 + anoter < 1800:
                        bot.send_message(message.from_user.id, kb3[2].text)

                if current_kb == "4":
                    if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1130:
                        bot.send_message(message.from_user.id, kb4[0].text)
                    if nexttime * 100 + anoter > 1130 and nexttime * 100 + anoter < 1630:
                        bot.send_message(message.from_user.id, kb4[1].text)
                    if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1130:
                        bot.send_message(message.from_user.id, kb4[2].text)
                    pos += 1
            flag = 1
            #bot.send_message(message.from_user.id, s)

        anoter = current_time.minute
        if s == "next" or anoter == 0: #какое занятие будет дальше

            for i in range(len(arr)):
                eventTime = arr[i].begin_h*100+arr[i].begin_m
                nowTime = nexttime *100 + anoter

                if nowTime > eventTime :
                    s = i
            flag = 1

            current_id = message.from_user.id
            if arr[s + 1].all_event == 0:


                if s+1 < len(arr):
                     bot.send_message(message.from_user.id, arr[s+1].text)
            else:
                    current_kb = 0
                    pos = 0

                    for j in users:
                        if j.id == current_id:
                            current_kb = j.kb
                            break
                    if current_kb == '1':
                        if nexttime*100 + anoter > 930 and nexttime*100 + anoter < 1130:
                            bot.send_message(message.from_user.id, kb1[1].text)
                        if nexttime*100 + anoter > 1130 and nexttime*100 + anoter < 1630:
                            bot.send_message(message.from_user.id, kb1[2].text)
                    if current_kb == '2':
                        if nexttime*100 + anoter > 930 and nexttime*100 + anoter < 1130:
                            bot.send_message(message.from_user.id, kb2[1].text)
                        if nexttime*100 + anoter > 1130 and nexttime*100 + anoter < 1630:
                            bot.send_message(message.from_user.id, kb2[2].text)

                    if current_kb == '3':
                        if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1130:
                            bot.send_message(message.from_user.id, kb3[1].text)
                        if nexttime * 100 + anoter > 1130 and nexttime * 100 + anoter < 1630:
                            bot.send_message(message.from_user.id, kb3[2].text)
                    if current_kb == "4":
                        if nexttime * 100 + anoter > 930 and nexttime * 100 + anoter < 1130:
                            bot.send_message(message.from_user.id, kb4[1].text)
                        if nexttime * 100 + anoter > 1130 and nexttime * 100 + anoter < 1630:
                            bot.send_message(message.from_user.id, kb4[2].text)

                    pos += 1


        if s == 'all':
            flag = 1
            pos = 0
            for i in arr:
                if i.all_event == 0:
                    bot.send_message(message.from_user.id, i.text)
                else:
                    current_kb = 0
                    current_id = message.from_user.id
                    for j in users:
                        if j.id == current_id:
                            current_kb = j.kb
                            break
                    #print(current_kb)
                    if current_kb == '1':
                        bot.send_message(message.from_user.id, kb1[pos].text)
                        # print("AAAAAAAAAAAAAAAAAAAAAAAAA")
                    if current_kb == '2':
                        bot.send_message(message.from_user.id, kb2[pos].text)
                    if current_kb == '3':
                        bot.send_message(message.from_user.id, kb3[pos].text)
                    if current_kb == "4":
                        bot.send_message(message.from_user.id, kb4[pos].text)
                    pos += 1



        if s == "lunch":
            flag = 1
            bot.send_message(message.from_user.id, NINE)
            bot.send_message(message.from_user.id, ELLEVEN)
            bot.send_message(message.from_user.id, FORTEEN)
            bot.send_message(message.from_user.id, FOR)
            bot.send_message(message.from_user.id, NINETEEN)
            bot.send_message(message.from_user.id, TWENTY )
        if s == 'скажи пожалуйста когда спать':
            flag = 1
            bot.send_message(message.from_user.id, "По идее спать можно в 22:00 и с 15:00 до 16:00, но ты можешь хоть сейчас")

        if s == 'спасибо':
            flag = 1
            bot.send_message(message.from_user.id, "Ага, всегда пожалуйста.")


        if flag == 0:
            bot.send_message(message.from_user.id, 'Ошибка, я не поняла запроса. Пожалуйста, повторите ещё раз')
    else:
        bot.send_message(message.from_user.id, "Ошибка, ты не зарегистрирован в моей базе данных. Пожалуйста, выполни регистрацию с помощью команды /reg")



bot.polling(none_stop=True)