import logging
from pyrogram import Client, filters

# Loggingni yoqish (terminalda barcha jarayonlarni ko'rish uchun)
logging.basicConfig(level=logging.INFO)

API_ID = 32318150
API_HASH = "98ec70eafb8aae142247bd0b0fbe8a96"

# Karta botining aniq username'i (@ belgisiz)
CARD_BOT_USERNAME = "CardXabarBot"

# Guruh ID raqami (yangi olingan superguruh ID)
WORKER_GROUP_ID = -1004453802443

app = Client("card_forwarder_session", api_id=API_ID, api_hash=API_HASH)


# CardXabar botidan kelgan xabarlarni guruhga yo'naltirish
@app.on_message(filters.chat(CARD_BOT_USERNAME))
async def forward_card_messages(client, message):
  print(f"\n📩 Xabar keldi! ID: {message.id}")
  try:
    await message.forward(chat_id=WORKER_GROUP_ID)
    print("✅ Guruhga muvaffaqiyatli yuborildi!")
  except Exception as e:
    print(f"❌ Guruhga yuborishda xatolik: {e}")


if __name__ == "__main__":
  print("🚀 Userbot ishga tushdi va xabarlarni kutmoqda...")
  app.run()