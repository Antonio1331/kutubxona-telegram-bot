from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_genre_buttons():
    keyboard = [
        [InlineKeyboardButton("📖 Badiiy", callback_data="genre_fiction")],
        [InlineKeyboardButton("🎓 Ilmiy", callback_data="genre_science")],
        [InlineKeyboardButton("👨‍💼 Biznes", callback_data="genre_business")],
        [InlineKeyboardButton("🕵️‍♂️ Detektiv", callback_data="genre_detective")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_book_actions(book_id):
    keyboard = [
        [InlineKeyboardButton("📥 Yuklab olish", callback_data=f"download_{book_id}")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="back_to_list")],
    ]
    return InlineKeyboardMarkup(keyboard)
