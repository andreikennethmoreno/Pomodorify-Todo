# Generated by Django 4.0.1 on 2024-03-30 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_rename_task_todo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='pomodoro',
        ),
    ]
