# Generated by Django 2.2.15 on 2020-09-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emojiapp', '0003_auto_20200919_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testentry',
            name='emoji',
        ),
        migrations.AddField(
            model_name='testentry',
            name='emoji',
            field=models.ManyToManyField(to='emojiapp.Emoji'),
        ),
    ]