from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest
from telethon.sync import events
import time, random
from app.models import user

ChannelName = 'labbad001'
ChannelName = 'https://t.me/sub4sub_group_for_YouTube'
ChannelName = ChannelName.split('/')[-1]
print(ChannelName)
# ChannelName = 'marathinaukrigroup'
msg = '''Hello guys,

Do you wants to increase :
20 Instagram follower or 100 Likes on post ?
Youtube subscriber 25 or 100Likes or 100Views or 10comment ?
and Want to boost your social media presence?
and earn cash at the same time?

t's easy! Just give a review on a Play Store app and send a screenshot of the given application link
Get amazing offers for each review, and even more for completing all of them!

1. https://play.google.com/store/apps/details?id=board.tictactoe.glow.game.lite
2. https://play.google.com/store/apps/details?id=com.photography.gallery.albums
3. https://play.google.com/store/apps/details?id=com.smart.filetransfer.shar

and just send me screen shot of given review
'''
class Command(BaseCommand):
    help = 'run in order to join'
    
    def handle(self,*args, **kwargs):
        userr =user.objects.all().order_by('?').first()
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
            print(members)
            print(len(members))
        except Exception as e : print(e)
        client.disconnect()
        for i in members : 
            try: 
                userr =user.objects.all().order_by('?').first()
                client = TelegramClient(f'./sessions/{userr.number}',userr.api_id,userr.api_hash)
                client.connect()
                try:
                    # if str(i.status) == 'UserStatusRecently()':
                    time.sleep(random.randint(5,9))
                    print(countt)
                    countt += 1
                    
                    if client.send_message(i,msg):
                        print(userr.username,'Has send message')
                    time.sleep(random.randint(5,9))
                except Exception as e : 
                    time.sleep(random.randint(5,9))
                    print(userr.username,'could not sent a message')
                    print(e)
                client.disconnect()
            except Exception as e:print(e)
