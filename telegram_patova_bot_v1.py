# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
  
   
# get your api_id, api_hash, token 
# from telegram as described above 

api_id = '1111111'
api_hash = '111111111111111111111111111'
token = '111111111:1111111111111111111111'

# your phone number 
phone = '+11111111111'
   
# creating a telegram session and assigning 
# it to a variable client 
client = TelegramClient('session', api_id, api_hash) 

# connecting and building the session 
client.connect() 
  
# in case of script ran first time it will 
# ask either to input token or otp sent to 
# number or sent or your telegram id  
if not client.is_user_authorized(): 
   
    #client.send_code_request(phone, force_sms=True) 
    client.send_code_request(phone)
    # signing in the client 
    client.sign_in(phone, input('Enter the code: ')) 
   
#user_to_patovear_Name = "@AAAAAAAA"
#user_to_patovear_Entity = client.get_entity(user_to_patovear_Name)

user_to_patovear_Name = "patovagroup"
#chat_url = "https://t.me/joinchat/11111111111111111111111111"
chat_url = "https://t.me/MYGROUP"
channel_entity = client.get_entity(chat_url)
#user_to_patovear_Name = "111111111111111111"

message = "Test de Nico - Patova_Bot"

try: 
    # receiver user_id and access_hash, use 
    # my user_id and access_hash for reference 
    #receiver = InputPeerUser(user_to_patovear_Name, user_to_patovear_Hash) 
  
    # sending message using telegram client 
    client.send_message(entity=user_to_patovear_Entity, message=message)
except Exception as e: 
      
    # there may be many error coming in while like peer 
    # error, wwrong access_hash, flood_error, etc 
    print(e); 
  
# disconnecting the telegram session  
client.disconnect() 
