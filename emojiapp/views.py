from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, filters, generics

from emojiapp.models import Emoji
from emojiapp.serializers import EmojiSerializer

from django.views.decorators.csrf import csrf_exempt

class SearchEmojiAPIView(generics.ListCreateAPIView):
	search_fields = ['emojiName']
	filter_backends = (filters.SearchFilter,)
	queryset = Emoji.objects.all()
	serializer_class = EmojiSerializer
