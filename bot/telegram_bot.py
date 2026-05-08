import json
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

FILE = "data/queries.json"

def load():
    try:
        return json.load(open(FILE))
    except:
        return []

def save(text):
    data = load()
    data.append(text)
    json.dump(data, open(FILE, "w"))

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save(update.message.text)
    await update.message.reply_text("OK")

def run(token):
    app = Application.builder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()
