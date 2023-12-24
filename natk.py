import time
import telebot, wikipedia, re
import telebot
import random
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('6967390123:AAEu28BRZ785-U_I2NkuvYKmSTnmHzuv2WA')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
CHANNEL_NAME = '@hahahanectod'

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
f = open('D:/ШАРАГА/OAP/fun.txt', 'r', encoding='UTF-8')
joke = f.read().split('\n')
f.close()    
@bot.message_handler(content_types=['haha'])
def handle_text(message):
     bot.send_message(CHANNEL_NAME, joke)
        
   
         
@bot.message_handler(commands=['name'])
def send_welcome(message):
    name = bot.get_me()
    print(name)
    bot.reply_to(message,f'Вы -{message.from_user.first_name} '  )
@bot.message_handler(commands=['id'])
def send_welcome(message):
    name = bot.get_me()
    print(name)
    bot.reply_to(message,f'Ваш id -{message.from_user.id} '  )

##CHANNEL_NAME = '@hahahanectod'
# Загружаем список шуток
#f = open('data/fun.txt', 'r', encoding='UTF-8')
#jokes = f.read().split('\n')
#f.close()
# Пока не закончатся шутки, посылаем их в канал
#for joke in jokes:
    #bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    #time.sleep(3600)
#bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)