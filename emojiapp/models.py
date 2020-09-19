from django.db import models
from django.utils import timezone

class Emoji(models.Model):
    emojiName = models.CharField(max_length=200)
    emoji = models.CharField(max_length=200)
    def __str__(self):
        return self.emojiName

class Meal(models.Model):
    mealName = models.CharField(max_length=200)
    def __str__(self):
        return self.mealName

class MealTime(models.Model):
    mealTimeName = models.CharField(max_length=200)
    def __str__(self):
        return self.mealTimeName

class TestEntry(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    emoji = models.ForeignKey('Emoji', on_delete=models.CASCADE)
    beforeAfter = models.ForeignKey('MealTime', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        # pylint: disable=E1101
        return self.emoji.emojiName
