# Generated by Django 4.0.5 on 2022-06-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemodel',
            name='diff',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=10),
        ),
    ]
