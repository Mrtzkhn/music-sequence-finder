# Generated by Django 5.1.4 on 2025-01-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_sequence', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midifile',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='midifile',
            name='fitness',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
