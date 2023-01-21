from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest, InviteToChannelRequest
from telethon.sync import events
import time, random
from app.models import user

ChannelName = 'https://t.me/freelancers_intl'
ChannelName = ChannelName.split('/')[-1]
print(ChannelName)
usernameLi = []
class Command(BaseCommand):
    def handle(self,*args, **kwargs):

        # userr = user.objects.all().
        userr =user.objects.all()[2]
        client = TelegramClient(f'./sessions/{userr.number}',userr.api_id,userr.api_hash)
        client.connect()
        try:
            if not client.is_user_authorized():
                client.send_code_request(phone=userr.number)
                otp = input('otp : ')
                client.sign_in(phone=userr.number,code=otp)
            

            client(JoinChannelRequest(ChannelName))
            entiy = client.get_entity(ChannelName)
            members = client.get_participants(entiy)
            countt = 0
            # print(members)
            
            for member in members:
                try:
                    usernamee = member.username
                    if usernamee :
                        usernameLi.append(member)
                except: ...
            
            print('total members :',len(usernameLi))
            for i in range(len(usernameLi)):
                try:
                    userentity = client.get_entity(usernameLi[i])
                    print(userentity,'--------------')
                    client(InviteToChannelRequest('side_hacks',[userentity]))
                    time.sleep(3)
                except Exception as e:
                    print(e)
            
            
        except Exception as e : print(e)
        client.disconnect()