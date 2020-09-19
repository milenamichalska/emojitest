# Generated by Django 2.2.15 on 2020-09-19 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emojiapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emoji',
            name='beforeAfter',
        ),
        migrations.RemoveField(
            model_name='emoji',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='emoji',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='emoji',
            name='user',
        ),
        migrations.CreateModel(
            name='TestEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beforeAfter', models.TextField()),
                ('meal', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('emoji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emojiapp.Emoji')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]