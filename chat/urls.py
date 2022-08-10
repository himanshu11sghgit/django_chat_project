from django.urls import path


from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('checkview/', views.checkview, name='checkview'),
    path('send/', views.send, name='send'),
    path('<str:room>/', views.room, name='room'),
    path('get-messages/<str:room>/', views.get_messages, name='get_messages'),
]