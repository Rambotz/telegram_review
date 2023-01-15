from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest
from telethon.sync import events
import time
ChannelName = 'labbad001'
ChannelName = 'English_dating_group_official'
# ChannelName = 'dating6'
msg = '''Offer Offer Offer
1. Get 100-200-300 Instagram likes absolutely free
---------------------- OR -------------------------
2. Get 5 youtube subscribers on your account.
---------------------- OR -------------------------
3. Earn 7 rupees on each review

Follow the steps below to avail this offer.

Step 1: https://wa.me/919662640635 Go to WhatsApp chat by clicking on this link and send the message by writing hi.

Step 2:
After sending Hi, then you will be given a link to the Google app and a text of the review.

Step 3:
After clicking on the link to download the application, give a 5-star rating, copy the review given to you and paste it into the app you downloaded on the google play store.

Step 4:
Then give a review and send its screenshot to that number and send it which offers you choice and if your choice is offer 1 or 2 then send a link related to that( if you want likes then send post links and if you want youtube scriber than send youtube profile link)

Step 5:
When your review goes live on the Google play store, you will get a message that 'You are rewarded' and if your choice is to offer 1 or 2 then you get to like or subscribe with in 24 hours. or if you choice offer 3 then you get paid on your UPI or Paytm.

Note:
( for offer 1:- After receiving the message, if your profile is private, it will be made public)

Forward your friends so that they can also take advantage of this offer and save this number in your phone for future offers.

join our telegram channel for more update:- https://t.me/passive_side_income
'''
class Command(BaseCommand):
    help = 'run in order to join'
    
    def handle(self,*args, **kwargs):
        number = 919978911838
        api_id = '14251965'
        api_hash = '5e489dc4ddfdf6b48db7240a20d84c57'
        client = TelegramClient(f'./sessions/{number}',api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone=number)
            otp = input('otp : ')
            client.sign_in(phone=number,code=otp)
        print(client.get_me().first_name)
        
        print(client(JoinChannelRequest(ChannelName)))
        entiy = client.get_entity(ChannelName)
        members = client.get_participants(entiy)
        print(members)
        for i in members : 
            try: 
                if str(i.status) == 'UserStatusRecently()':
                    time.sleep(3)
                    print('yes')
                    print(client.send_message(i,msg))
            except Exception as e:print(e)