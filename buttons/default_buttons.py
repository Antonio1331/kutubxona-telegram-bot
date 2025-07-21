from telegram import ReplyKeyboardMarkup

def main_menu():
    keyboard = [
        ['📚 Kitoblar', '📖 Janrlar'],
        ['ℹ️ Yordam', '📞 Aloqa']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
