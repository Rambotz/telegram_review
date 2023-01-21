from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest
from telethon.sync import events
import time, random
ChannelName = 'labbad001'
ChannelName = 'English_dating_group_official'
# ChannelName = 'marathinaukrigroup'
msg = '''Heyy miss,
'''
class Command(BaseCommand):
    help = 'run in order to join'
    
    def handle(self,*args, **kwargs):
        number = 918849926680
        api_id = '28520110'
        api_hash = 'd5f3306768ffb2a3dc7ac373d38cafe9'
        client = TelegramClient(f'./sessions/{number}',api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone=number)
            otp = input('otp : ')
            client.sign_in(phone=number,code=otp)
        print(client.get_me().first_name)
        
        print(client(JoinChannelRequest(ChannelName)))
        entiy = client.get_entity(ChannelName)
        members = client.get_participants(entiy)[200:]
        countt = 0
        print(members)
        print(len(members))
        
        for i in members : 
            try: 
                # if str(i.status) == 'UserStatusRecently()':
                time.sleep(random.randint(10,18))
                print(countt)
                countt += 1
                print(client.send_message(i,msg))
            except Exception as e:print(e)
