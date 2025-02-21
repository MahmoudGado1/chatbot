# Generated by Django 4.2.15 on 2024-11-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0002_alter_message_chat"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="type",
            field=models.CharField(
                choices=[("human", "Human"), ("ai", "Ai")],
                default="human",
                max_length=120,
            ),
            preserve_default=False,
        ),
    ]
