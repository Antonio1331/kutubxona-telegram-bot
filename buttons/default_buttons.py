from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_menu_buttons():
    keyboard = [
        [KeyboardButton("📚 Kitoblar ro'yxati")],
        [KeyboardButton("🔎 Janrlar bo'yicha")],
        [KeyboardButton("📩 Bog'lanish")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
