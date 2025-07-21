from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📚 Katalog", callback_data="catalog"))
    markup.add(InlineKeyboardButton("📞 Bog‘lanish", callback_data="contact"))
    return markup
