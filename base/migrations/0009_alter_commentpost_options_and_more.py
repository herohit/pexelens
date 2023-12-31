# Generated by Django 4.1.7 on 2023-07-12 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_notification_comment_detail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentpost',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
