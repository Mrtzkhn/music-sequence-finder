# Generated by Django 5.1.4 on 2025-01-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_sequence', '0006_midifile_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midifile',
            name='sequence',
            field=models.CharField(max_length=200, null=True),
        ),
    ]