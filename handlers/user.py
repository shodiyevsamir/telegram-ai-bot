from ai import ask_ai
from database import save_user, is_allowed, is_premium
from config import ADMIN_ID
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(m):
        save_user(m.from_user.id)
        bot.send_message(m.chat.id, "Salom! AI bot 🤖")

    @bot.message_handler(func=lambda m: True)
    def chat(m):
        user_id = m.from_user.id

        # ❌ RUXSAT YO‘Q BO‘LSA
        if not is_allowed(user_id) and not is_premium(user_id):

            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("✅ Allow", callback_data=f"allow_{user_id}"),
                InlineKeyboardButton("⏳ 1h", callback_data=f"allowtime_{user_id}")
            )
            markup.add(
                InlineKeyboardButton("❌ Deny", callback_data=f"deny_{user_id}")
            )

            # userga javob
            try:
                bot.send_message(m.chat.id, "⛔ Sizga hali ruxsat berilmagan!")
            except Exception as e:
                print("USERGA XATO:", e)

            # admin ga yuborish (MUHIM FIX)
            try:
                bot.send_message(
                    ADMIN_ID,
                    f"📩 Yangi AI so‘rov:\n\nUser ID: {user_id}\nText: {m.text}",
                    reply_markup=markup
                )
            except Exception as e:
                print("ADMINGA XATO:", e)

            return

        # ✅ RUXSAT BOR
        try:
            reply = ask_ai(m.text)

            try:
                bot.send_message(m.chat.id, reply)
            except Exception as e:
                print("USERGA JAVOB XATO:", e)

        except Exception as e:
            print("AI XATO:", e)

            try:
                bot.send_message(m.chat.id, "Xatolik chiqdi 😅")
            except:
                pass
