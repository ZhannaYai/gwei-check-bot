import requests
import time
import telebot

# Set up Telegram bot
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Set up Ethereum Gas Station API
url = 'https://ethgasstation.info/api/ethgasAPI.json'

# Define command handler
@bot.message_handler(commands=['follow'])
def follow_command(message):
    # Parse Gwei value from message text
    try:
        gwei_value = int(message.text.split()[1])
    except:
        bot.reply_to(message, "Please enter a valid Gwei value to follow.")
        return

    # Save Gwei value to file
    with open('gwei_value.txt', 'w') as f:
        f.write(str(gwei_value))

    # Send confirmation message
    bot.reply_to(message, f"Successfully set Gwei value to {gwei_value}. You will now receive alerts when the Gwei value falls below {gwei_value}.")

# Polling loop
while True:
    # Fetch Gwei value from API
    response = requests.get(url)
    data = response.json()
    gwei_value = data['fast']

    # Check if Gwei value is below threshold
    with open('gwei_value.txt', 'r') as f:
        threshold = int(f.read())
    if gwei_value < threshold:
        message = f"Gwei value is {gwei_value}. ALERT!"
        bot.send_message('YOUR_TELEGRAM_CHAT_ID', message)

    # Polling interval
    time.sleep(300)

# Start polling
bot.polling()
