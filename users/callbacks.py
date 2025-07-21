import json
from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

def handle_callback(bot, call: CallbackQuery):
    if call.data == "catalog":
        bot.answer_callback_query(call.id)

        try:
            with open("database/books.json", "r", encoding="utf-8") as f:
                books = json.load(f)

            if not books:
                bot.send_message(call.message.chat.id, "📚 Katalog hozircha bo‘sh.")
                return

            markup = InlineKeyboardMarkup()
            for i, book in enumerate(books):
                btn_text = f"{book['title']} – {book['author']}"
                callback = f"book_{i}"
                markup.add(InlineKeyboardButton(btn_text, callback_data=callback))

            bot.send_message(call.message.chat.id, "📚 Katalogdan kitobni tanlang:", reply_markup=markup)

        except FileNotFoundError:
            bot.send_message(call.message.chat.id, "❌ Katalog fayli topilmadi.")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"❌ Xatolik yuz berdi: {e}")

    elif call.data == "contact":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📞 Biz bilan bog‘lanish uchun: +998 90 123 45 67")


    elif call.data.startswith("book_"):
        index = int(call.data.split("_")[1])
        with open("database/books.json", "r", encoding="utf-8") as f:
            books = json.load(f)

        if index < len(books):
            book = books[index]
            text = f"📖 Siz tanlagan kitob:\n\nNomi: {book['title']}\nMuallif: {book['author']}"
            bot.send_message(call.message.chat.id, text)
