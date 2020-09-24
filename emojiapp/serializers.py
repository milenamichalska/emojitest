from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Emoji, TestEntry, Meal, MealTime


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = ['emojiName', 'emoji']

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['mealName']

class MealTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealTime
        fields = ['mealTimeName']

class TestEntrySerializer(serializers.ModelSerializer):
    emoji = EmojiSerializer(read_only=True, many=True)
    class Meta:
        model = TestEntry
        fields = ['user', 'emoji', 'meal', 'beforeAfter', 'created_date']
