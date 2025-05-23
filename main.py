from telegram.ext import ApplicationBuilder
from handlers import start_handler, lang_handler, text_handler
from config import BOT_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(start_handler)
app.add_handler(lang_handler)
app.add_handler(text_handler)

print("Bot is running...")
app.run_polling()