from telebot.types import Message
from buttons.inline_buttons import get_main_menu

def start_command(bot, message: Message):
    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Quyidagi menyudan birini tanlang:",
        reply_markup=get_main_menu()
    )
