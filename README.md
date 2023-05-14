# gwei-check-bot
Telegram bot that sends an alert when the Gwei value is less than some value

This code listens for the /follow command in Telegram messages and expects the Gwei value to be provided as a parameter (e.g., /follow 30). If the Gwei value is valid, it is saved to a file and a confirmation message is sent back to the user. The code then polls the Ethereum Gas Station API every 5 minutes and sends an alert to the user's Telegram chat if the Gwei value falls below the threshold value saved in the file.

You'll need to replace YOUR_TELEGRAM_BOT_TOKEN and YOUR_TELEGRAM_CHAT_ID with your actual bot token and chat ID.
