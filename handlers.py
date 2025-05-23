from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from language import get_text, user_language
from gmail_generator import generate_gmail

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_language[user_id] = 'en'
    keyboard = get_text(user_id, 'keyboard')
    await update.message.reply_text(get_text(user_id, 'start'), reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    if 'বাংলা' in text:
        user_language[user_id] = 'bn'
    else:
        user_language[user_id] = 'en'
    await start(update, context)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    if '➕' in text:
        first, email, password, recovery = generate_gmail()
        message = get_text(user_id, 'gmail_info').format(first=first, email=email, password=password, recovery=recovery)
        await update.message.reply_text(message)

start_handler = CommandHandler("start", start)
lang_handler = MessageHandler(filters.Regex("বাংলা|English"), lang)
text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)