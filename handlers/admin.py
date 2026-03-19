from config import ADMIN_ID
from database import allow_user

def register(bot):

    @bot.message_handler(commands=['allow'])
    def allow(m):
        if m.from_user.id != ADMIN_ID:
            return

        try:
            user_id = int(m.text.split()[1])
            allow_user(user_id)

            bot.send_message(user_id, "✅ Sizga AI ishlatish ruxsati berildi!")
            bot.send_message(m.chat.id, "Ruxsat berildi ✅")

        except:
            bot.send_message(m.chat.id, "Xato format! /allow USER_ID")
