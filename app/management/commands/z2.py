from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest
from telethon.sync import events
import time, random
from app.models import user

ChannelName = 'labbad001'
ChannelName = 'English_dating_group_official'
# ChannelName = 'marathinaukrigroup'
msg = '''Heyy miss,
'''
class Command(BaseCommand):
    help = 'run in order to join'
    
    def handle(self,*args, **kwargs):
        
        userr = user.objects.all()
        for user_ in userr:
            print(user_.username)
            number = input('Number :')
            user_.number = number
            user_.save()
        