from config import ADMIN_ID
from database import get_users

def register(bot):

    @bot.message_handler(commands=['users'])
    def users(m):
        if m.from_user.id == ADMIN_ID:
            users = get_users()
            bot.send_message(m.chat.id, f"Foydalanuvchilar soni: {len(users)}")
        
