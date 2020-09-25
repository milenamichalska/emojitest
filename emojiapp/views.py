from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, filters, generics

from emojiapp.models import Emoji, Meal, MealTime, TestEntry
from emojiapp.serializers import EmojiSerializer, MealSerializer, MealTimeSerializer, TestEntrySerializer

from django.views.decorators.csrf import csrf_exempt

class SearchEmojiAPIView(generics.ListCreateAPIView):
	search_fields = ['emojiName']
	filter_backends = (filters.SearchFilter,)
	queryset = Emoji.objects.all()
	serializer_class = EmojiSerializer

class MealsAPIView(generics.ListCreateAPIView):
	queryset = Meal.objects.all()
	serializer_class = MealSerializer

class MealTimesAPIView(generics.ListCreateAPIView):
	queryset = MealTime.objects.all()
	serializer_class = MealTimeSerializer

class TestEntryAPIView(generics.ListCreateAPIView):
	queryset = TestEntry.objects.all()
	serializer_class = TestEntrySerializer
