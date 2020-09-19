from django.shortcuts import render
from .models import Emoji, TestEntry
from django.db.models import Count

def emoji_test(request):
    emojis = Emoji.objects.annotate(count=Count('testentry')).order_by('count')
    return render(request, 'emojitest/emojitest.html', {'emojis': emojis})
