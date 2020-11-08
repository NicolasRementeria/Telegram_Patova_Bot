import requests
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
  
def telegram_bot_sendtext(chat_id, bot_message):
    bot_token = 'AAAAAAAAAA:AAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    #bot_chatID = 'AAAAAAAA'
    #bot_chatID = "AAAAAAAAA"
    #send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

#test = telegram_bot_sendtext(str(channel_entity.access_hash), "Testing Telegram bot")
test = telegram_bot_sendtext(str(-11111111111111), "Testing Telegram bot")

print(test)