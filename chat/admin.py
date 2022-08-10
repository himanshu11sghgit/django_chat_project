from django.contrib import admin



from .models import Room, Message

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'msg', 'created_at', 'room', 'user']