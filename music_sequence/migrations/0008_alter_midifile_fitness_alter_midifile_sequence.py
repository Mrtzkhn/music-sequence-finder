# Generated by Django 5.1.4 on 2025-01-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_sequence', '0007_alter_midifile_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midifile',
            name='fitness',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='midifile',
            name='sequence',
            field=models.CharField(default='', max_length=200),
        ),
    ]
