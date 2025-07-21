from telebot.types import CallbackQuery


def handle_callback(bot, call: CallbackQuery):
    if call.data == "catalog":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📚 Bu yerda katalog mavjud emas hozircha.")

    elif call.data == "contact":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📞 Biz bilan bog‘lanish uchun: +998 90 123 45 67")
