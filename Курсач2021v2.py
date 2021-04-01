# Підключаємо модуль для Телеграма(бот)
import telebot
# Імпортуємо типи з модуля, щоб створювати кнопки
from telebot import types
# Підключаємо модуль для POWM
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
#Змінюємо мову на українську
config_dict = get_default_config()
config_dict['language'] = 'UK'
#POWM код
owm = OWM('19994b52f6f2b8be125eff9eb16e2041', config_dict )
mgr = owm.weather_manager()
#TeleBot код
bot = telebot.TeleBot("1622518490:AAFHGHNPNloplhpe1rwrRoo5-zdp1YMLF78", parse_mode=None,)
#Реакція на команду старт
@bot.message_handler(commands=['start'])
def welcome(message):
    # Створюємо клавіатуру Reply
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton('/start')
    help = types.KeyboardButton('/help')
    developer = types.KeyboardButton('/developer')
    user_markup.row(start, help)
    user_markup.row(developer)
    # Привітання
    sti = open('static/welcome.webp', 'rb')#rb = открыть бинарный файл на чтение. r = Read, b - Binary
    bot.send_sticker(message.chat.id, sti, reply_markup = user_markup)
    bot.send_message(message.chat.id, "Ласкаво просимо, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений щоб бути піддослідним кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html')
    # Створюємо клавіатуру Inline
    keyboard = types.InlineKeyboardMarkup()
    # По черзі готуємо текст і обробник для кожного міста
    key_Vinnytsia = types.InlineKeyboardButton(text='🌤 Вінниця', callback_data='pogoda')
    key_Lutsk = types.InlineKeyboardButton(text='🌤 Луцьк', callback_data='pogoda1')
    key_Dnipro = types.InlineKeyboardButton(text='🌤 Дніпро', callback_data='pogoda2')
    key_Donetsk = types.InlineKeyboardButton(text='🌤 Донецьк', callback_data='pogoda3')
    key_Zhytomyr = types.InlineKeyboardButton(text='🌤 Житомир', callback_data='pogoda4')
    key_Uzhhorod = types.InlineKeyboardButton(text='🌤 Ужгород', callback_data='pogoda5')
    key_Zaporizhzhia = types.InlineKeyboardButton(text='🌤 Запоріжжя', callback_data='pogoda6')
    key_IvanoFrankivsk = types.InlineKeyboardButton(text='🌤 Івано-Франківськ', callback_data='pogoda7')
    key_Kyiv = types.InlineKeyboardButton(text='🌤 Київ', callback_data='pogoda8')
    key_Kropyvnytskyi = types.InlineKeyboardButton(text='🌤 Кропивницький', callback_data='pogoda9')
    key_Lugansk = types.InlineKeyboardButton(text='🌤 Луганськ', callback_data='pogoda10')
    key_lviv = types.InlineKeyboardButton(text='🌤 Львів', callback_data='pogoda11')
    key_Mykolaiv = types.InlineKeyboardButton(text='🌤 Миколаїв', callback_data='pogoda12')
    key_Odessa = types.InlineKeyboardButton(text='🌤 Одеса', callback_data='pogoda13')
    key_Poltava = types.InlineKeyboardButton(text='🌤 Полтава', callback_data='pogoda14')
    key_Rivne = types.InlineKeyboardButton(text='🌤 Рівне', callback_data='pogoda15')
    key_Sumy = types.InlineKeyboardButton(text='🌤 Суми', callback_data='pogoda16')
    key_Ternopil = types.InlineKeyboardButton(text='🌤 Тернопіль', callback_data='pogoda17')
    key_Kharkiv = types.InlineKeyboardButton(text='🌤 Харків', callback_data='pogoda18')
    key_Kherson = types.InlineKeyboardButton(text='🌤 Херсон', callback_data='pogoda19')
    key_Khmelnytskyi = types.InlineKeyboardButton(text='🌤 Хмельницький', callback_data='pogoda20')
    key_Cherkasy = types.InlineKeyboardButton(text='🌤 Черкаси', callback_data='pogoda21')
    key_Chernivtsi = types.InlineKeyboardButton(text='🌤 Чернівці', callback_data='pogoda22')
    key_Chernihiv = types.InlineKeyboardButton(text='🌤 Чернігів', callback_data='pogoda23')
    # Вивод коноки кажного міста
    keyboard.add(key_Vinnytsia, key_Lutsk, key_Dnipro)
    keyboard.add(key_Donetsk, key_Zhytomyr, key_Uzhhorod)    
    keyboard.add(key_Zaporizhzhia, key_IvanoFrankivsk, key_Kyiv)
    keyboard.add(key_Kropyvnytskyi, key_Lugansk, key_lviv)
    keyboard.add(key_Mykolaiv, key_Odessa, key_Poltava)
    keyboard.add(key_Rivne, key_Sumy, key_Ternopil)
    keyboard.add(key_Kharkiv, key_Kherson, key_Khmelnytskyi)
    keyboard.add(key_Cherkasy, key_Chernivtsi, key_Chernihiv)
    bot.send_message(message.chat.id,'Натисніть кнопку мені або напишіть населений пункт.', reply_markup=keyboard)
#Реакція бота на команду 'help'
@bot.message_handler(commands=['help'])
def help(message):    
    sti = open('static/cat1.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ можу показувати погоду по всьому світу\n/start - Обласні центри України або напишіть мені населений пункт.\n/developer - розробник бота".format(message.from_user, bot.get_me()),
        parse_mode='html')
#Реакція бота на команду 'developer'
@bot.message_handler(commands=['developer'])
def help(message):   
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти в Instagram ", url="https://www.instagram.com/denchik.shelenko/")
    keyboard.add(url_button) 
    sti = open('static/developer.webp', 'rb')
    bot.send_sticker(message.chat.id, sti, reply_markup=keyboard)
    bot.send_message(message.chat.id, "Щоб повернутися натисніть кнопку :\n/start - Головне меню\n/help - допомога")
#Реакція бота на текст
@bot.message_handler(content_types=['text'])
def get_text_messages(message): 
    try:
        #ввід міста з клавіатури
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В населеному пункті " + message.text + " зараз " + w.detailed_status + "\n\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(message.chat.id, answer )

    except:
        bot.send_message(message.chat.id, 'Помилка! Такого міста не існує.\nПеревірте правильність написання.\nМісто має бути вказано без зайвих символів.\nПриклад : "Лондон" - правильно "Лондон." - не правильно')
# Оброблювач натискань на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "pogoda": 
        #надсилання стікеру з данним містом
        sti = open('static/city/Vinnytsia.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Вінниця')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Вінниця' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda1":
        #надсилання стікеру з данним містом
        sti = open('static/city/Lutsk.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Луцьк')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Луцьк' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer) 
    elif call.data == "pogoda2":
        #надсилання стікеру з данним містом
        sti = open('static/city/Dnipro.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Дніпро')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
           #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Дніпро' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)   
    elif call.data == "pogoda3":
        #надсилання стікеру з данним містом
        sti = open('static/city/Donetsk.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Донецьк')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Донецьк' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda4":
        #надсилання стікеру з данним містом
        sti = open('static/city/Zhytomyr.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Житомир')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Житомир' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda5":
        #надсилання стікеру з данним містом
        sti = open('static/city/Uzhhorod.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Ужгород')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Ужгород' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda6":
        #надсилання стікеру з данним містом
        sti = open('static/city/Zaporizhzhia.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Запоріжжя')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Запоріжжя' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)      
    elif call.data == "pogoda7":
        #надсилання стікеру з данним містом
        sti = open('static/city/IvanoFrankivsk.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Івано-Франківськ')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Івано-Франківськ' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)       
    elif call.data == "pogoda8":
        #надсилання стікеру з данним містом
        sti = open('static/city/Kyiv.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Київ')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Київ' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda9":
        #надсилання стікеру з данним містом
        sti = open('static/city/Kropyvnytskyi.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Кропивницький')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Кропивницький' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)      
    elif call.data == "pogoda10":
        #надсилання стікеру з данним містом
        sti = open('static/city/Lugansk.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Луганськ')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Луганськ' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)       
    elif call.data == "pogoda11":
        #надсилання стікеру з данним містом
        sti = open('static/city/lviv.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Львів')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Львів' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)        
    elif call.data == "pogoda12":
        #надсилання стікеру з данним містом
        sti = open('static/city/Mykolaiv.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Миколаїв')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Миколаїв' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)           
    elif call.data == "pogoda13":
        #надсилання стікеру з данним містом
        sti = open('static/city/Odessa.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Одеса')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Одеса' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)                
    elif call.data == "pogoda14":
        #надсилання стікеру з данним містом
        sti = open('static/city/Poltava.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Полтава')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Полтава' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)       
    elif call.data == "pogoda15":
        #надсилання стікеру з данним містом
        sti = open('static/city/Rivne.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Рівне')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Рівне' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"    
    elif call.data == "pogoda16":
        #надсилання стікеру з данним містом
        sti = open('static/city/Sumy.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Суми')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Суми' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)      
    elif call.data == "pogoda17":
        #надсилання стікеру з данним містом
        sti = open('static/city/Ternopil.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Тернопіль')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Тернопіль' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)   
    elif call.data == "pogoda18":
        #надсилання стікеру з данним містом
        sti = open('static/city/Kharkiv.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Харків')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Харків' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)      
    elif call.data == "pogoda19":
        #надсилання стікеру з данним містом
        sti = open('static/city/Kherson.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Херсон')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Херсон' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)       
    elif call.data == "pogoda20":
        #надсилання стікеру з данним містом
        sti = open('static/city/Khmelnytskyi.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Хмельницький')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Хмельницький' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda21":
        #надсилання стікеру з данним містом
        sti = open('static/city/Cherkasy.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Черкаси')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Черкаси' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda22":
        #надсилання стікеру з данним містом
        sti = open('static/city/Chernivtsi.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Чернівці')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Чернівці' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "pogoda23":
        #надсилання стікеру з данним містом
        sti = open('static/city/Chernihiv.webp', 'rb')
        bot.send_sticker(call.message.chat.id, sti)
        observation = mgr.weather_at_place('Чернігів')
        w = observation.weather
        #Температура
        temp = w.temperature('celsius')["temp"]
        #Вітер
        wind = w.wind()["speed"]
        #Вологість
        humi = w.humidity
        #Хмарність
        cl = w.clouds
        #Час
        ti = w.reference_time('iso')
        answer = " В місті " + 'Чернігів' + " зараз " + w.detailed_status + "\n"
        answer += " Температура в місті   " + str(temp) + "°C" + "\n\n"
        answer += " Вітер   " + str(wind) + " м/с" + "\n\n"
        answer += " Вологість   " + str(humi) + "%" + "\n\n"
        answer += " Хмарність   " + str(cl) + "%" + "\n\n"
        answer += " Час   " + str(ti) + "\n\n"
        if temp < 5: 
            answer += " Зараз холодно. Одягнітся, тепліше!\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        elif temp < 10:
            answer += "Зараз холодно. Одягнітся по тепліше\n\n" 
            answer += "Натиснiть на кнопку для подальшого користування: /start"
        else:
            answer += "Сьогодні тепло. Одягнітся легше\n\n"
            answer += "Натиснiть на кнопку для подальшого користування: /start" 
        bot.send_message(call.message.chat.id, answer)
# Запускаємо постійне опитування бота в Телеграма
bot.polling( none_stop = True, interval=0)