import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="miau miau :3")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def main():
    bot = telegram.Bot(token='523645972:AAGxsjnwVFKbnqnG_EJURnWiBKdOLa--5XI')
    updater = Updater(token='523645972:AAGxsjnwVFKbnqnG_EJURnWiBKdOLa--5XI')
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    echo_handler = MessageHandler(Filters.text, echo)
    print(bot.get_me())
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":

    main()