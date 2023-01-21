from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest
from telethon.sync import events
from app.models import user

class Command(BaseCommand):
    help = 'run in order to join'
    
    def handle(self,*args, **kwargs):
        
        number = 918000238427
        api_id = '25929829'
        api_hash = '0199268ddc9dec0c09cc2bc3c1705bc0'
        client = TelegramClient(f'./sessions/{number}',api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            
            client.send_code_request(phone=number)
            otp = input('otp : ')
            if client.sign_in(phone=number,code=otp):
                print('user is successfully signed in')
            else:
                print('please provide details correct')
        else : 
            print('This user is already exists')
            
        if client.is_user_authorized():
            me = client.get_me()
            print(me.first_name)
            user_details, created = user.objects.get_or_create(
                api_hash = api_hash,
                api_id=api_id,
                username = me.username
            )
            print('User :',user_details)
            print('user created :',created)
        print(client.get_me().username)
        client.disconnect()