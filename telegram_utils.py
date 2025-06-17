from telegram import Bot

# Bot tokens (replace with your actual tokens)
TRUECALLER_BOT_TOKEN = 'YOUR_TRUECALLER_BOT_TOKEN'
CLOUDUPLOAD_BOT_TOKEN = 'YOUR_CLOUDUPLOAD_BOT_TOKEN'

# Chat ID (bot's private group/channel where response is handled)
DEFAULT_CHAT_ID = 'YOUR_CHANNEL_OR_USER_ID'  # Can be a group ID or user ID

def send_to_telegram_bot(option, user_input):
    if option == "truecaller":
        bot = Bot(TRUECALLER_BOT_TOKEN)
    elif option == "cloudupload":
        bot = Bot(CLOUDUPLOAD_BOT_TOKEN)
    else:
        return "Invalid option selected"

    # Send message to Telegram bot
    bot.send_message(chat_id=DEFAULT_CHAT_ID, text=f"INPUT: {user_input}")
    return "Message sent to bot"
