from django.urls import path
from . import views


urlpatterns =[
    path("",views.Chat,name="Chat"),
    path('<str:room_name>/', views.room, name='room'),
]