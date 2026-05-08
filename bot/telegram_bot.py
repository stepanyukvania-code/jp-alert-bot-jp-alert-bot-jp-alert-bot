from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from data.store import load_queries, save_queries

TOKEN = None


async def start(update, context):
    await update.message.reply_text("Bot started. Use /add /list /remove")


async def add(update, context):
    q = " ".join(context.args).strip()
    if not q:
        await update.message.reply_text("Usage: /add iphone")
        return

    data = load_queries()

    if q not in data:
        data.append(q)
        save_queries(data)

    await update.message.reply_text(f"Added: {q}")


async def list_q(update, context):
    data = load_queries()
    await update.message.reply_text("\n".join(data) if data else "Empty")


async def remove(update, context):
    q = " ".join(context.args).strip()
    data = load_queries()

    if q in data:
        data.remove(q)
        save_queries(data)

    await update.message.reply_text(f"Removed: {q}")


def run(token):
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", list_q))
    app.add_handler(CommandHandler("remove", remove))

    app.run_polling()
