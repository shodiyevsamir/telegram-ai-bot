from ai import ask_ai
from database import save_user, is_allowed
from config import ADMIN_ID

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(m):
        save_user(m.from_user.id)
        bot.send_message(m.chat.id, "Salom! AI botga xush kelibsiz 🤖")

    @bot.message_handler(func=lambda m: True)
    def chat(m):
        user_id = m.from_user.id

        if not is_allowed(user_id):
            bot.send_message(m.chat.id, "⛔ Sizga hali ruxsat berilmagan!")

            bot.send_message(
                ADMIN_ID,
                f"📩 Yangi AI so‘rov:\n\nUser ID: {user_id}\nText: {m.text}\n\n/allow {user_id}"
            )
            return

        try:
            reply = ask_ai(m.text)
            bot.send_message(m.chat.id, reply)
        except Exception as e:
            print(e)
            bot.send_message(m.chat.id, "Xatolik chiqdi 😅")
