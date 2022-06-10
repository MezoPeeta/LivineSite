# Generated by Django 3.2.6 on 2022-06-10 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RecipesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, null=True)),
                ('type_in_arabic', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='directions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='directions_in_arabic',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='time_taken',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='type_in_arabic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='difficulty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.difficulty'),
        ),
    ]
