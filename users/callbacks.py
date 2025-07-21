import json
from data.loader import bot


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "catalog":
        with open("database/books.json", "r", encoding="utf-8") as f:
            books = json.load(f)

        for book in books:
            text = f"<b>{book['title']}</b>\nMuallif: {book['author']}\nNarxi: {book['price']}"
            bot.send_message(call.message.chat.id, text, parse_mode="HTML")

    elif call.data == "contact":
        bot.send_message(call.message.chat.id, "Bog‘lanish uchun: @admin_username")
