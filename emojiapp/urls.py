from django.urls import path
from . import views

urlpatterns = [
    path('', views.emoji_test, name='emojitest'),
]
