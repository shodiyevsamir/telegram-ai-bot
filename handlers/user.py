from ai import ask_ai
from database import save_user

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(m):
        save_user(m.from_user.id)
        bot.send_message(m.chat.id, "Salom! AI bot ishlayapti 🤖")

    @bot.message_handler(func=lambda m: True)
    def chat(m):
        try:
            reply = ask_ai(m.text)
            bot.send_message(m.chat.id, reply)
        except Exception as e:
            bot.send_message(m.chat.id, "Xatolik chiqdi 😅")
            print(e)
