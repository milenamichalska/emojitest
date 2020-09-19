from django.shortcuts import render

def emoji_test(request):
    return render(request, 'emojitest/emojitest.html', {})
