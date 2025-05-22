import telebot
import os

# Inizializza il bot con il tuo token
API_TOKEN = os.getenv("BOT_TOKEN")  # Sicurezza: lo leggeremo da Render, non in chiaro nel codice
bot = telebot.TeleBot(API_TOKEN)

# ID dei gruppi e loro nomi simbolici
groups = {
    -1001234567890: "Taglio",
    -1009876543210: "Pulizia",
    -1001928374650: "Traduzione",
    -1005647382910: "Scrittura"
}

# Funzione di saluto e verifica connessione
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "✨ Bot attivo, amore! Pronto a registrare tutto. ✂️🧽📝🖊️")

# Funzione principale per loggare i messaggi
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    sender = message.from_user.first_name or "Utente"
    text = message.text

    if chat_id in groups:
        gruppo = groups[chat_id]
        print(f"📥 Messaggio da {gruppo} | {sender}: {text}")
        # Qui salveremo anche in database o su Google Sheets in futuro

        # Placeholder: rispondiamo con conferma
        bot.reply_to(message, f"Ricevuto, {sender}! Ho registrato il tuo messaggio per il gruppo {gruppo} ✨")

# Avvia il bot
print("Bot in ascolto...")
bot.infinity_polling()

