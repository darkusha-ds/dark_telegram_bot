from datetime import time, date, datetime
import telebot as tg
import config

bot = tg.TeleBot(config.token_test)

#      0      1      2      3      4      5      6      7      8
num = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ']
#      0              1           2            3          4              5          6         7               8           9       10             11             12           13          14
sub = ['Математика ', 'Русс.яз ', 'Общество ', 'Физика ', 'Литература ', 'Физ-ра ', 'Химия ', 'Информатика ', 'История ', 'ОБЖ ', 'Астрономия ', 'География ',  'Биология ', 'Англ.яз ', 'Самообр.']
#       0        1         2         3          4         5          6               7
type = ['база ', 'проф. ', 'база 1 ', 'проф. 1 ', 'база 2 ', 'проф. 2 ', ' (общ. проф) ', ' (общ. база) ']
#      0      1      2      3      4      5      6      7      8      9      10     11     12     13     14     15     16
cab = ['102', '110', '115', '123', '201', '203', '209', '217', '220', '309', '311', '321', '322', '319', '317', '216', '202']
#     0              1                      2          3              4                  5          6          7          8              9          10             11             12
pc = ['220/201/322', '110/123/201/308/322', '220/102', '220/311/102', '110/123/308/102', '201/322', '311/102', '201/220', '210/311/102', '220/322', '220/210/102', '220/301/102', '217/322']
#     0        1        2        3        4        5        6       7       8
cl = ['(10а)', '(10б)', '(10в)', '(11а)', '(11б)', '(11в)', '10а-', '10б-', '10в-']
#      0      1
ili = [' / ', '/']
#     0                     1
pr = ['(проф.Орловой Е.В)', '(проф.Лазепной Е.В)']
#      0матеша база;   1матеша проф;   2общество база; 3общество проф; 4физика база;   5физика проф;   6химия база;    7химия проф;    8история база;  9история проф;  10географ база;  11географ проф;  12биология база; 13биология проф;
pop = [sub[0]+type[0], sub[0]+type[1], sub[2]+type[0], sub[2]+type[1], sub[3]+type[0], sub[3]+type[1], sub[6]+type[0], sub[6]+type[1], sub[8]+type[0], sub[8]+type[1], sub[11]+type[0], sub[11]+type[1], sub[12]+type[0], sub[12]+type[1]]

time = [
    '1. 8:30 - 9:10 (10) \n',
    '2. 9:20 - 10:00 (15) \n',
    '3. 10:15 - 10:55 (15) \n',
    '4. 11:10 - 11:50 (15) \n',
    '5. 12:05 - 12:45 (10) \n',
    '6. 12:55 - 13:35 (25) \n',
    '7. 14:00 - 14:40 (15) \n',
    '8. 14:55 - 15:35 (15) \n',
    '9. 15:50 - 16:30 \n'
]
d = ['Расписание на понедельник \n \n']
########################################################################################################################
# day1_10_1 = [num[0] + sub[7] + cab[5]]
day1_10_1 = [num[0] + 'НИЧЕГО']
day1_10_2 = [num[1] + pop[3] + cab[4] + ili[0] + pop[7] + cab[11]]
day1_10_3 = [num[2] + pop[3] + cab[4] + ili[0] + pop[7] + cab[11]]
day1_10_4 = [num[3] + sub[1] + pc[0]]
day1_10_5 = [num[4] + sub[4] + pc[0]]
day1_10_6 = [num[5] + sub[4] + pc[0]]
day1_10_7 = [num[6] + sub[13] + pc[1]]
day1_10_8 = [num[7] + pop[0] + cab[12] + ili[0] + sub[5] + cab[2] + pr[0]]
day1_10_9 = [num[8] + pop[0] + cab[12] + ili[0] + sub[5] + cab[2] + pr[0]]

day2_10_1 = [num[0] + pop[1] + pc[5] + ili[0] + sub[7] + cab[5]]
day2_10_2 = [num[1] + pop[2] + cab[12] + ili[1] + pop[4] + cab[4] + type[6] + ili[1] + sub[7] + cab[5]]
day2_10_3 = [num[2] + pop[2] + cab[12] + ili[1] + pop[4] + cab[4] + type[6]]
day2_10_4 = [num[3] + pop[3] + cab[12] + ili[1] + pop[4] + cab[4] + type[7]]
day2_10_5 = [num[4] + pop[3] + cab[12] + ili[1] + pop[4] + cab[4] + type[7] + ili[1] + sub[7] + cab[5]]
day2_10_6 = [num[5] + sub[6] + type[2] + cab[11] + ili[1] + sub[8] + type[4] + cab[4] + ili[1] + sub[7] + cab[5]]
day2_10_7 = [num[6] + sub[6] + type[4] + cab[11] + ili[1] + sub[8] + type[2] + cab[4] + ili[1] + sub[7] + cab[5]]
day2_10_8 = [num[7] + pop[0] + cab[12] + ili[1] + sub[5] +cab[2] + pr[1] + ili[1] + sub[7] + cab[5]]
day2_10_9 = [num[8] + pop[0] + cab[12] + ili[1] + sub[5] +cab[2] + pr[1]]

day3_10_1 = [num[0] + pop[13] + cab[12] + ili[1] + pop[9] + cab[4] + ili[1] + pop[11] + cab[8]]
day3_10_2 = [num[1] + pop[9] + cab[4] + ili[1] + pop[11] + cab[8]]
day3_10_3 = [num[2] + sub[1] + pc[0]]
day3_10_4 = [num[3] + sub[1] + pc[0]]
day3_10_5 = [num[4] + pop[1] + pc[7]]
day3_10_6 = [num[5] + pop[1] + pc[7]]
day3_10_7 = [num[6] + sub[4] + pc[0]]
day3_10_8 = [num[7] + pop[0] + cab[12]]

day4_10_1 = [num[0] + sub[7] + cab[5]]
day4_10_2 = [num[1] + pop[1] + pc[9]]
day4_10_3 = [num[2] + pop[1] + pc[9]]
day4_10_4 = [num[3] + sub[14] + cab[8] + cl[0] + ili[1] + sub[10] + cab[4] + cl[1] + ili[1] + sub[9] + cab[12] + cl[2]]
day4_10_5 = [num[4] + sub[9] + cab[8] + cl[0] + ili[1] + sub[14] + cab[4] + cl[1] + ili[1] + sub[10] + cab[12] + cl[2]]
day4_10_6 = [num[5] + sub[10] + cab[8] + cl[0] + ili[1] + sub[9] + cab[4] + cl[1] + ili[1] + sub[14] + cab[12] + cl[2]]
day4_10_7 = [num[6] + pop[7] + cab[10] + ili[1] + pop[5] + cab[12] + ili[1] + pop[11] + cab[4] + ili[1] + pop[9] + cab[6]]
day4_10_8 = [num[7] + pop[13] + cab[14] + ili[1] + pop[5] + cab[12] + ili[1] + pop[9] + cab[6]]
day4_10_9 = [num[8] + pop[13] + cab[14] + ili[1] + pop[5] + cab[12]]

day5_10_1 = [num[0] + pop[1] + pc[12]]
day5_10_2 = [num[1] + pop[1] + pc[12]]
day5_10_3 = [num[2] + sub[13] + cl[6] + cab[15] + ili[1] + cl[7] + cab[4] + ili[1] + cl[8] + cab[12]]
day5_10_4 = [num[3] + sub[13] + cl[6] + cab[16] + ili[1] + cl[7] + cab[4] + ili[1] + cl[8] + cab[12]]
day5_10_5 = [num[4] + sub[11] + type[2] + cab[12] + ili[1] + sub[8] + type[4] + cab[4]]
day5_10_6 = [num[5] + sub[11] + type[4] + cab[12] + ili[1] + sub[8] + type[2] + cab[4]]
day5_10_7 = [num[6] + pop[12] + pc[5]]


day1_10 = [day1_10_1[0] + '\n' + day1_10_2[0] + '\n' + day1_10_3[0] + '\n' + day1_10_4[0] + '\n' + day1_10_5[0] + '\n' + day1_10_6[0] + '\n' + day1_10_7[0] + '\n' + day1_10_8[0] + '\n' + day1_10_9[0]]
day2_10 = [day2_10_1[0] + '\n' + day2_10_2[0] + '\n' + day2_10_3[0] + '\n' + day2_10_4[0] + '\n' + day2_10_5[0] + '\n' + day2_10_6[0] + '\n' + day2_10_7[0] + '\n' + day2_10_8[0] + '\n' + day2_10_9[0]]
day3_10 = [day3_10_1[0] + '\n' + day3_10_2[0] + '\n' + day3_10_3[0] + '\n' + day3_10_4[0] + '\n' + day3_10_5[0] + '\n' + day3_10_6[0] + '\n' + day3_10_7[0] + '\n' + day3_10_8[0]]
day4_10 = [day4_10_1[0] + '\n' + day4_10_2[0] + '\n' + day4_10_3[0] + '\n' + day4_10_4[0] + '\n' + day4_10_5[0] + '\n' + day4_10_6[0] + '\n' + day4_10_7[0] + '\n' + day4_10_8[0] + '\n' + day4_10_9[0]]
day5_10 = [day5_10_1[0] + '\n' + day5_10_2[0] + '\n' + day5_10_3[0] + '\n' + day5_10_4[0] + '\n' + day5_10_5[0] + '\n' + day5_10_6[0] + '\n' + day5_10_7[0]]

# #======================================================================================================================#

day1_11_1 = [num[0] + pop[7] + cab[10] + ili[1] + pop[9] + cab[0]]
day1_11_2 = [num[1] + pop[13] + cab[12] + ili[1] + pop[9] + cab[0] + ili[1]+ sub[7] + cab[5]]
day1_11_3 = [num[2] + pop[13] + cab[12] + ili[1] + pop[9] + cab[0] + ili[1]+ sub[7] + cab[5]]
day1_11_4 = [num[3] + pop[3] + cab[0] + pop[7] + cab[10] + ili[1]+ sub[7] + cab[5]]
day1_11_5 = [num[4] + pop[3] + cab[0] + ili[1]+ sub[7] + cab[5]]
day1_11_6 = [num[5] + sub[11] + type[2] + cab[10] + ili[1] + sub[8] + type[4] + cab[0] + ili[1]+ sub[7] + cab[5]]
day1_11_7 = [num[6] + sub[11] + type[4] + cab[10] + ili[1] + sub[8] + type[2] + cab[0] + ili[1]+ sub[7] + cab[5]]
day1_11_8 = [num[7] + sub[9] + cab[0] + cl[4] + ili[1] + sub[5] + cab[2] + cl[5]]
day1_11_9 = [num[8] + sub[5] + cab[2] + cl[5]]

day2_11_1 = [num[0] + sub[1] + pc[2]]
day2_11_2 = [num[1] + sub[0] + pc[3]]
day2_11_3 = [num[2] + sub[0] + pc[3]]
day2_11_4 = [num[3] + sub[4] + pc[3]]
day2_11_5 = [num[4] + sub[4] + pc[3]]
day2_11_6 = [num[5] + sub[13] + pc[4]]
day2_11_7 = [num[6] + sub[13] + pc[4]]
day2_11_8 = [num[7] + sub[5] + cab[2] + cl[3]]
day2_11_9 = [num[8] + sub[5] + cab[2] + cl[3]]

day3_11_1 = [num[0] + pop[1] + pc[6]]
day3_11_2 = [num[1] + pop[2] + cab[10] + ili[1] + pop[4] + cab[0] + type[6]]
day3_11_3 = [num[2] + pop[2] + cab[10] + ili[1] + pop[4] + cab[0] + type[6]]
day3_11_4 = [num[3] + pop[3] + cab[10] + ili[1] + pop[4] + cab[0] + type[7]]
day3_11_5 = [num[4] + pop[3] + cab[10] + ili[1] + pop[4] + cab[0] + type[7]]
day3_11_6 = [num[5] + sub[6] + type[2] + cab[10] + ili[1] + sub[8] + type[4] + cab[0]]
day3_11_7 = [num[6] + sub[6] + type[4] + cab[10] + ili[1] + sub[8] + type[2] + cab[0]]
day3_11_8 = [num[7] + sub[9] + cab[0] + cl[3] + ili[1] + sub[5] + cab[2] + cl[4]]
day3_11_9 = [num[8] + sub[5] + cab[2] + cl[4]]

day4_11_1 = [num[0] + pop[5] + cab[0] + ili[1] + pop[7] + cab[10]]
day4_11_2 = [num[1] + pop[11] + cab[0] + ili[1] + pop[5] + cab[10]]
day4_11_3 = [num[2] + pop[11] + cab[0] + ili[1] + pop[5] + cab[10]]
day4_11_4 = [num[3] + pop[1] + pc[6]]
day4_11_5 = [num[4] + sub[0] + pc[8]]
day4_11_6 = [num[5] + pop[9] + cab[6]]
day4_11_7 = [num[6] + pop[13] + cab[13]]

day5_11_1 = [num[0] + sub[1] + pc[2]]
day5_11_2 = [num[1] + sub[1] + pc[10]]
day5_11_3 = [num[2] + sub[0] + pc[3]]
day5_11_4 = [num[3] + sub[0] + pc[3]]
day5_11_5 = [num[4] + sub[4] + pc[11]]
day5_11_6 = [num[5] + pop[12] + pc[6]]
day5_11_7 = [num[6] + sub[13] + pc[4]]
day5_11_8 = [num[7] + sub[9] + cab[0] + cl[5]]


day1_11 = [day1_11_1[0] + '\n' + day1_11_2[0] + '\n' + day1_11_3[0] + '\n' + day1_11_4[0] + '\n' + day1_11_5[0] + '\n' + day1_11_6[0] + '\n' + day1_11_7[0] + '\n' + day1_11_8[0] + '\n' + day1_11_9[0]]
day2_11 = [day2_11_1[0] + '\n' + day2_11_2[0] + '\n' + day2_11_3[0] + '\n' + day2_11_4[0] + '\n' + day2_11_5[0] + '\n' + day2_11_6[0] + '\n' + day2_11_7[0] + '\n' + day2_11_8[0] + '\n' + day2_11_9[0]]
day3_11 = [day3_11_1[0] + '\n' + day3_11_2[0] + '\n' + day3_11_3[0] + '\n' + day3_11_4[0] + '\n' + day3_11_5[0] + '\n' + day3_11_6[0] + '\n' + day3_11_7[0] + '\n' + day3_11_8[0] + '\n' + day3_11_9[0]]
day4_11 = [day4_11_1[0] + '\n' + day4_11_2[0] + '\n' + day4_11_3[0] + '\n' + day4_11_4[0] + '\n' + day4_11_5[0] + '\n' + day4_11_6[0] + '\n' + day4_11_7[0]]
day5_11 = [day5_11_1[0] + '\n' + day5_11_2[0] + '\n' + day5_11_3[0] + '\n' + day5_11_4[0] + '\n' + day5_11_5[0] + '\n' + day5_11_6[0] + '\n' + day5_11_7[0] + '\n' + day5_11_8[0]]

########################################################################################################################

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Здравствуй, приятно с тобой познакомиться. Если нужна будет помощь по работе со мной, то просто напиши мне /help и я тебе все объясню')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'Мои команды: \n \n' + '/about - что-то обо мне \n' + '10 - расписание 10-го класса \n' + '11 - расписание 11-го класса \n' + 'завтра 10 - посмотреть расписание 10-х на завтра \n' + 'завтра 11 - посмотреть расписание 11-х на завтра \n' + "звонки - список всех звонков" )

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, f'Я - бот, который умеет отправлять расписание, если тебе будет нужна помощь по командам, напиши /help, и я отправлю список команд, которые я понимаю')

@bot.message_handler(content_types=['text'])
def send_lessons(message):
    if message.text.lower() == '10':
        if date.today().weekday() == 0:
            bot.send_message(message.chat.id, "".join(day1_10))
        if date.today().weekday() == 1:
            bot.send_message(message.chat.id, "".join(day2_10))
        if date.today().weekday() == 2:
            bot.send_message(message.chat.id, "".join(day3_10))
        if date.today().weekday() == 3:
            bot.send_message(message.chat.id, "".join(day4_10))
        if date.today().weekday() == 4:
            bot.send_message(message.chat.id, "".join(day5_10))
        if date.today().weekday() == 5:
            bot.reply_to(message, 'Хоть сегодня выходной, но могу подсказать расписание на понедельник')
            bot.send_message(message.chat.id, d[0] + "".join(day1_10))
        if date.today().weekday() == 6:
            bot.reply_to(message, 'Хоть сегодня выходной, но могу подсказать расписание на понедельник')
            bot.send_message(message.chat.id, d[0] + "".join(day1_10))

    elif message.text.lower() == '11':
        if date.today().weekday() == 0:
            bot.send_message(message.chat.id, "".join(day1_11))
        if date.today().weekday() == 1:
            bot.send_message(message.chat.id, "".join(day2_11))
        if date.today().weekday() == 2:
            bot.send_message(message.chat.id, "".join(day3_11))
        if date.today().weekday() == 3:
            bot.send_message(message.chat.id, "".join(day4_11))
        if date.today().weekday() == 4:
            bot.send_message(message.chat.id, "".join(day5_11))
        if date.today().weekday() == 5:
            bot.reply_to(message, 'Хоть сегодня выходной, но могу подсказать расписание на понедельник')
            bot.send_message(message.chat.id, d[0] + "".join(day1_11))
        if date.today().weekday() == 6:
            bot.reply_to(message, 'Хоть сегодня выходной, но могу подсказать расписание на понедельник')
            bot.send_message(message.chat.id, d[0] + "".join(day1_11))

    elif message.text.lower() == 'завтра 10':
        if date.today().weekday() == 0:
            bot.reply_to(message, 'Расписание на вторник')
            bot.send_message(message.chat.id, "".join(day2_10))
        if date.today().weekday() == 1:
            bot.reply_to(message, 'Расписание на среду')
            bot.send_message(message.chat.id, "".join(day3_10))
        if date.today().weekday() == 2:
            bot.reply_to(message, 'Расписание на четверг')
            bot.send_message(message.chat.id, "".join(day4_10))
        if date.today().weekday() == 3:
            bot.reply_to(message, 'Расписание на пятницу')
            bot.send_message(message.chat.id, "".join(day5_10))
        if date.today().weekday() == 4:
            bot.reply_to(message, 'Расписание на понедельник')
            bot.send_message(message.chat.id, "".join(day1_10))
        if date.today().weekday() == 5:
            bot.reply_to(message, 'Хоть завтра и выходной, но могу подсказать расписание на понедельник')
            bot.send_message(message.chat.id, d[0] + "".join(day1_10))
        if date.today().weekday() == 6:
            bot.send_message(message.chat.id, d[0] + "".join(day1_10))

    elif message.text.lower() == 'завтра 11':
        if date.today().weekday() == 0:
            bot.reply_to(message, 'Расписание на вторник')
            bot.send_message(message.chat.id, "".join(day2_11))
        if date.today().weekday() == 1:
            bot.reply_to(message, 'Расписание на среду')
            bot.send_message(message.chat.id, "".join(day3_11))
        if date.today().weekday() == 2:
            bot.reply_to(message, 'Расписание на четверг')
            bot.send_message(message.chat.id, "".join(day4_11))
        if date.today().weekday() == 3:
            bot.reply_to(message, 'Расписание на пятницу')
            bot.send_message(message.chat.id, "".join(day5_11))
        if date.today().weekday() == 4:
            bot.reply_to(message, 'Расписание на понедельник')
            bot.send_message(message.chat.id, "".join(day1_11))
        if date.today().weekday() == 5:
            bot.reply_to(message, 'Хоть завтра и выходной, но могу подсказать расписание на понедельник')
            bot.send_message(message.chat.id, d[0] + "".join(day1_11))
        if date.today().weekday() == 6:
            bot.send_message(message.chat.id, d[0] + "".join(day1_11))


    elif message.text.lower() == 'звонки':
        bot.reply_to(message, "".join(time))

    else:
        bot.send_message(message.from_user.id, 'Ошибка, я не понял запроса. Пожалуйста, повторите ещё раз')
# Обязательное условие!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)