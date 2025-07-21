from telebot.types import Message

def handle_text(bot, message: Message):
    bot.send_message(message.chat.id, "Iltimos, tugmalardan birini tanlang.")