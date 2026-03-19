from config import ADMIN_ID
from database import allow_user, get_allowed_users, add_premium

def register(bot):

    # 🔘 INLINE BUTTON HANDLER
    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):

        if call.from_user.id != ADMIN_ID:
            return

        data = call.data

        # ✅ DOIMIY RUXSAT
        if data.startswith("allow_"):
            user_id = int(data.split("_")[1])
            allow_user(user_id)

            bot.send_message(user_id, "✅ Sizga doimiy ruxsat berildi!")

            bot.edit_message_text(
                f"✅ Doimiy ruxsat berildi: {user_id}",
                call.message.chat.id,
                call.message.message_id
            )

        # ⏳ 1 SOATLIK RUXSAT
        elif data.startswith("allowtime_"):
            user_id = int(data.split("_")[1])
            allow_user(user_id, duration=3600)

            bot.send_message(user_id, "⏳ Sizga 1 soatlik ruxsat berildi!")

            bot.edit_message_text(
                f"⏳ 1 soat ruxsat berildi: {user_id}",
                call.message.chat.id,
                call.message.message_id
            )

        # ❌ RAD ETISH
        elif data.startswith("deny_"):
            user_id = int(data.split("_")[1])

            bot.send_message(user_id, "❌ Sizga ruxsat berilmadi")

            bot.edit_message_text(
                f"❌ Rad etildi: {user_id}",
                call.message.chat.id,
                call.message.message_id
            )

    # 📊 RUXSAT OLAR RO‘YXATI
    @bot.message_handler(commands=['allowed'])
    def allowed_list(m):
        if m.from_user.id != ADMIN_ID:
            return

        users = get_allowed_users()
        text = "📊 Ruxsat berilganlar:\n\n"

        for u in users:
            text += f"{u}\n"

        bot.send_message(m.chat.id, text)

    # 💸 PREMIUM QO‘SHISH
    @bot.message_handler(commands=['premium'])
    def premium(m):
        if m.from_user.id != ADMIN_ID:
            return

        try:
            user_id = int(m.text.split()[1])
            add_premium(user_id)

            bot.send_message(user_id, "💎 Siz premium bo‘ldingiz!")
            bot.send_message(m.chat.id, "Qo‘shildi ✅")
        except:
            bot.send_message(m.chat.id, "Format: /premium ID")
