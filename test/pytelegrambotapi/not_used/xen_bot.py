import telebot as tg
import random
import config

class user:
	def __init__(self, name, id):
		self.name = name
		self.id = id



bot = tg.TeleBot(config.token_vanya)




users = []

path = []
path.append("/home/izackfostar/python/kurva/hen")
path.append("/home/izackfostar/python/kurva/hen2")
path.append("/home/izackfostar/python/kurva/hen3")
path.append("/home/izackfostar/python/kurva/hen4")
path.append("/home/izackfostar/python/kurva/hen5")
path.append("/home/izackfostar/python/kurva/hen6")
path.append("/home/izackfostar/python/kurva/hen7")
path.append("/home/izackfostar/python/kurva/hen8")
path.append("/home/izackfostar/python/kurva/hen9")
path.append("/home/izackfostar/python/kurva/hen10")
path.append("/home/izackfostar/python/kurva/hen11")
path.append("/home/izackfostar/python/kurva/hen12")
path.append("/home/izackfostar/python/kurva/hen13")
path.append("/home/izackfostar/python/kurva/hen14")
path.append("/home/izackfostar/python/kurva/hen15")
path.append("/home/izackfostar/python/kurva/hen16")
path.append("/home/izackfostar/python/kurva/hen17")
path.append("/home/izackfostar/python/kurva/hen18")
path.append("/home/izackfostar/python/kurva/hen19")
path.append("/home/izackfostar/python/kurva/hen20")
my_choice = random.choice(path)




def check(current_id): # функция которая проверяет зарегистрирован ли человек
    for i in users:
        if i.id == current_id:
            return 1
    return 0


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message, f"Здарова! Я бот, который будет отправлять тебе только отборную порнуху! Зарегистрируйся ВО МНЕ с помощью команды /reg")

@bot.message_handler(commands=["reg"])
def other_name(message):
    global user_id #глобальная переменная хранящая id зарегистрировшегося пользователя
    
    user_id = message.from_user.id # принятие информации из текста, который отправляет пользователь
    if check(user_id) == 1: #если такой id уже зарегистрирован, то не дает зарегистрироваться воторой раз
        print("Кто-то проходит регистрацию повторно")
        bot.reply_to(message, f"Введи новый ник")
    else:
        bot.reply_to(message, f"Пожалуйста введи свой так называемый в высшем интернете \"ник-нейм\" Однако лучше всего будет, если вы зарегистрируетесь под своим именем")
    bot.register_next_step_handler(message, get_name)
def get_name(message):
	global name
	name = message.text.lower()
	users.append(user(name, user_id))
	bot.reply_to(message, f"Ты зарегистрирован в моей базе данных. Теперь чтобы стать испорченным тебе надо ввести команду \"хен\" с маленькой буквы и идти расчехляться")
	print(users[len(users) - 1].name)
	print(users[len(users) - 1].id)


@bot.message_handler(content_types=['text'])
def vladik(message):
	
	send = message.from_user.id
	s = message.text.lower()
	
	if (s == "привет") or (s == "Привет"):
		bot.send_message(send, 'ЗДРАВСТВУЙ, СЛАДКАЯ')
	if (s == "хен"):
		bot.send_photo(send, open(random.choice(path), 'rb'));




bot.polling(none_stop=True)