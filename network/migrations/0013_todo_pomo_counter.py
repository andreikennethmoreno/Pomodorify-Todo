# Generated by Django 4.0.1 on 2024-04-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_delete_chek_todo_pomodoro'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='pomo_counter',
            field=models.IntegerField(default=0),
        ),
    ]
