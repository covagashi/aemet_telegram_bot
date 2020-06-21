from telegram.ext import Updater
from telegram.ext import CommandHandler
import threading
import aemet
import datetime
import schedule
import conf_management as ConfMgt
import os
PORT = int(os.environ.get("PORT", "8443"))



def start(bot, update):
    message = "Bienvenido, {}".format(update.effective_user.username) + " Te diré el tiempo cada mañana, también puedes usar el comando /weather para solicitar el tiempo actual"
    bot.send_message(chat_id=update.message.chat_id, text=message))


def hello(bot, update):
    greeting = "Hola, {}".format(update.effective_user.username)    
    bot.send_message(chat_id=update.message.chat_id, text=greeting)


def weather(bot, update):
    ok = False
    result_text = ''

    ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token())

    if not ok:
        bot.send_message(chat_id=update.message.chat_id, text='Error al conectar con AEMET')
    else:
        bot.send_message(chat_id=update.message.chat_id, text=result_text)


def main(bot_token):
    """ Main function of the bot """
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Command handlers
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)    
    weather_handler = CommandHandler('weather', weather)

    # Add the handlers to the bot
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(add_handler)    
    dispatcher.add_handler(weather_handler)

    # Starting the bot for webhook  
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=bot_token)
    updater.bot.setWebhook('https://YOUR APP NAME HERE.herokuapp.com/' + bot_token)
    updater.idle()


def envia_telegram(bot_token, id_chat, texto_enviar):
    update = Updater(token=bot_token)
    update.bot.send_message(chat_id=id_chat, text=texto_enviar)


def check_weather():
    ok = False
    result_text = ''

    ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token())

    if not ok:
        envia_telegram(ConfMgt.get_telegram_token(), ConfMgt.get_telegram_group_id(), 'Error al conectar con AEMET')
    else:
        envia_telegram(ConfMgt.get_telegram_token(), ConfMgt.get_telegram_group_id(), result_text)


if __name__ == "__main__":
    main(ConfMgt.get_telegram_token())
    schedule.every().day.at('07:00').do(check_weather)

    
