from bot import telegram_chatbot
import database
import telebot
bot = telegram_chatbot("config.cfg")
tb = telebot.TeleBot('925315384:AAFDFxw79PytN584M5AYYbtGsRNlCBhIBr0')
iden =None
update_id = None

def make_reply(msg):
    reply = None
    if msg is not None:
        reply = database.text(iden,msg)
    return reply


#@tb.message_handler(commands=['start', 'go'])
def start_handler(message):
    msg = tb.send_message(message.chat.id, "Привет, отправь логин и пароль")
    iden= database.is_user(msg)
    if iden is None:  # если такой комбинации не существует, ждём команды /start Опять
        tb.send_message(message.chat.id, r'Неправильно введен логин\пароль')



while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            if iden is None :
                iden = database.is_user(message)
            else:
                reply = make_reply(message)
                bot.send_message(reply, from_)

