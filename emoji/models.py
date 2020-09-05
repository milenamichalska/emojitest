from django.db import models
from django.utils import timezone


class Emoji(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    emojiName = models.CharField(max_length=200)
    emoji = models.CharField(max_length=200)
    beforeAfter = models.TextField()
    meal = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.emojiName