from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from emojiapp.models import Emoji
from emojiapp.serializers import EmojiSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_emojis(request):
	data = Emoji.objects.all()
	if request.method == 'GET':
		serializer = EmojiSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

# from django.shortcuts import render
# from .models import Emoji, TestEntry
# from django.db.models import Count

# def emoji_test(request):
#     emojis = Emoji.objects.annotate(count=Count('testentry')).order_by('count')
#     return render(request, 'emojitest/emojitest.html', {'emojis': emojis})
