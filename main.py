import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from env.py import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued"""
    update.message.reply_text("Hi!")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued"""
    update.message.reply_text("Help!")

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message"""
    update.message.reply_text(update.message.text)

def reverse_echo(update: Update, context: CallbackContext) -> None:
    """Echo the user reversed message"""
    update.message.reply_text(update.message.text[::-1])


def main():
    """Start the bot"""
    # Create the Updater and pass it your bot's token
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e. message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reverse_echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
