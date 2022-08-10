import json


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


from .models import Room, Message

# Create your views here.



def home(request):
    return render(request, 'home.html')
    
    
def room(request, room):
    print('she')
    username = request.GET.get('username')
    room = Room.objects.get(name=room)
    context = {
        'username': username,
        'room': room,
    }
    return render(request, 'room.html', context)


def checkview(request):
    if request.method == 'POST':
        room = request.POST.get('room_name')
        username = request.POST.get('username')

        if Room.objects.filter(name=room).exists():
            return redirect('/' + room + '/?username=' + username)
        else:
            Room.objects.create(name=room)
            return redirect('/' + room + '/?username=' + username)
    else:
        return redirect('/')


def send(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')
        message = request.POST.get('message')
        
        message = Message.objects.create(msg=message, user=username, room=room_id)
        
        return HttpResponse('message send successfully')



def get_messages(request, room):
    room = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room.id)

    data = {
        'messages': list(messages.values())
    }
    # print('messages', messages)

    return JsonResponse(data)