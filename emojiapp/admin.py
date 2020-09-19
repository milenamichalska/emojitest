from django.contrib import admin
from .models import Emoji, TestEntry, Meal, MealTime

admin.site.register(Emoji)
admin.site.register(TestEntry)
admin.site.register(Meal)
admin.site.register(MealTime)
