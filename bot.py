from telebot import TeleBot
from config import BOT_TOKEN

from handlers import user, admin, support

bot = TeleBot(BOT_TOKEN)

user.register(bot)
admin.register(bot)
support.register(bot)

print("Bot ishga tushdi 🚀")
bot.infinity_polling()
