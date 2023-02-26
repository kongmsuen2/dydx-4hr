import requests
from decouple import config


# Send Message
def send_message(message):
    bot_token1 = config("TELEGRAM_TOKEN")
    chat_id1 = config("TELEGRAM_CHAT_ID")
    url1 = f"https://api.telegram.org/bot{bot_token1}/sendMessage?chat_id={chat_id1}&text={message}"
    res1 = requests.get(url1)
