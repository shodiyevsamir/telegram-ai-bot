from config import ADMIN_ID

def register(bot):

    @bot.message_handler(commands=['support'])
    def support_cmd(m):
        text = m.text.replace("/support", "").strip()

        if not text:
            bot.send_message(m.chat.id, "Xabar yozing: /support salom")
            return

        bot.send_message(ADMIN_ID, f"📩 Yangi murojaat:\n\n{text}")
        bot.send_message(m.chat.id, "Yuborildi ✅")
