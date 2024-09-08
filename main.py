import telebot
import random
import json
import os
from telebot import types

# Initialize the bot with your token
bot = telebot.TeleBot('7375816473:AAE34HP0HJW5gy2mEupjLVikZ6Z421JZM1k')

# Define possible predictions
result = ["👉Big👈", "👉Small👈", "👉 Red 🔴 👈", "👉 Green 🟢 👈"]

# Path to the JSON file
AUTHORIZED_USERS_FILE = 'authorized_users.json'

def load_authorized_users():
    """Load authorized users from the JSON file."""
    if not os.path.isfile(AUTHORIZED_USERS_FILE):
        # Create file with empty list if it doesn't exist
        with open(AUTHORIZED_USERS_FILE, 'w') as file:
            json.dump({"authorized_users": []}, file)
        return set()
    
    with open(AUTHORIZED_USERS_FILE, 'r') as file:
        data = json.load(file)
        return set(data.get('authorized_users', []))

def save_authorized_users(users):
    """Save authorized users to the JSON file."""
    data = {'authorized_users': list(users)}
    with open(AUTHORIZED_USERS_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Load authorized users from file
AUTHORIZED_USERS = load_authorized_users()

def is_authorized(user_id):
    """Check if a user is authorized."""
    return user_id in AUTHORIZED_USERS

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if is_authorized(message.from_user.id):
        bot.reply_to(message, "Please enter the last 3 digits of the period number.")
    else:
        user_id = message.from_user.id
        bot.reply_to(message, f"You are not authorized to use this bot.\nYour user ID is: {user_id}")
        keyboard = types.InlineKeyboardMarkup()
        join_button = types.InlineKeyboardButton(text="Godwin🔐", url="https://t.me/greyhat_forest")
        keyboard.add(join_button)
        bot.send_message(message.chat.id, "Support", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if is_authorized(message.from_user.id):
        if len(message.text) == 3 and message.text.isdigit():
            prediction = random.choice(result)
            bot.reply_to(message, f"\n\nNEXT PREDICTION IS: {prediction}")
        else:
            bot.reply_to(message, "Invalid input. Please enter the last 3 digits of the period number.")
    else:
        bot.reply_to(message, "You are not authorized to use this bot.")

bot.polling()

