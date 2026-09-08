import os
import threading
from fastapi import FastAPI
import uvicorn
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", "10000"))

web = FastAPI()

@web.get("/")
async def home():
    return {"status": "online", "bot": "Telegram"}

def run_web():
    uvicorn.run(web, host="0.0.0.0", port=PORT)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fala! 🤖 Bot funcionando!")

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponíveis:\n"
        "/start - iniciar\n"
        "/ajuda - mostrar ajuda"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ajuda", ajuda))

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    print("Bot online!")
    app.run_polling()
