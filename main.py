import telebot
from telebot import types

# Initialize the bot with your token
bot = telebot.TeleBot('7525252627:AAGc_NEVAWChST5O_WkBMCLhVeaYlFnaeGw')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create an inline keyboard with three "Join" buttons
    keyboard = types.InlineKeyboardMarkup()
    join_button1 = types.InlineKeyboardButton(text="Free hack❤️ ", url="https://t.me/trust_me_brother")
    join_button2 = types.InlineKeyboardButton(text="Help❤️", url="https://t.me/mafiya_bhai_support")
    join_button3 = types.InlineKeyboardButton(text="FF ID❤️", url="https://t.me/demo_account_super")
    join_button4 = types.InlineKeyboardButton(text="Owner❤️", url="https://t.me/rdx_mafiya_000")
    join_button5 = types.InlineKeyboardButton(text="Bot Developer❤️", url="https://t.me/greyhat_forest")
    keyboard.add(join_button1, join_button2, join_button3, join_button4, join_button5)

    bot.reply_to(message, "🥹 You must join our channels to access exclusive content.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Echo the received message text
    bot.reply_to(message, f"You said: {message.text}")

# Start polling to receive messages
bot.polling(none_stop=True)
