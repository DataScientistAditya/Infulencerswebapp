from django.contrib.auth import login
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from .models import MessageData
from App.models import Influencer_Details, Details_Advertiser
from App.Utility import Chat_Room_Adv, Chat_Rooms_Inf

# Create your views here.


def Chat(request):
    return render(request,'chat/Chat.html')

@login_required
def room(request, room_name):
    try:
        Profile_Pic = Influencer_Details.objects.all().filter(User = request.user.id).values('Profile_Picture')[0]['Profile_Picture']
        Rooms = Chat_Rooms_Inf(User_Id=request.user.id)
    except:
        Profile_Pic = Details_Advertiser.objects.all().filter(User = request.user.id).values('Profile_Picture')[0]['Profile_Picture']
        Rooms = Chat_Room_Adv(User_id=request.user.id)
        
    Profile_Url = "../../media/{}".format(Profile_Pic)
    Messefes_PREV = MessageData.last_20_messages(room_name=room_name)
    return render(request, 'chat/RoomChat.html', {
        'room_name': room_name,
        'username': request.user.username,
        'msg': Messefes_PREV,
        'Pic':Profile_Url,
        "Contacts":Rooms
    })
    
    
