# Generated by Django 3.2.6 on 2022-06-10 22:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220611_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 22, 15, 24, 315582, tzinfo=utc)),
        ),
    ]