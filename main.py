import telebot
from users.commands import start_command
from users.callbacks import handle_callback
from users.text_handlers import handle_text
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    start_command(bot, message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    handle_callback(bot, call)

@bot.message_handler(func=lambda message: True)
def handle_all_text(message):
    handle_text(bot, message)

if __name__ == "__main__":
    bot.infinity_polling()