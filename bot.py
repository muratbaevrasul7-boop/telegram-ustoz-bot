from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = ""
USTOZ_CHAT_ID =

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    text = (
        f"👤 Student: {user.full_name}\n"
        f"🔗 Username: @{user.username}\n"
    )

    await context.bot.send_message(
        chat_id=USTOZ_CHAT_ID,
        text=text
    )

    if update.message.document:
        await context.bot.send_document(
            chat_id=USTOZ_CHAT_ID,
            document=update.message.document.file_id
        )

    if update.message.photo:
        await context.bot.send_photo(
            chat_id=USTOZ_CHAT_ID,
            photo=update.message.photo[-1].file_id
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handler))
app.run_polling()
