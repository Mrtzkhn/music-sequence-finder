# Generated by Django 5.1.4 on 2025-01-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MidiFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a descriptive title for the MIDI file.', max_length=255)),
                ('midi_file', models.FileField(help_text='Upload a valid MIDI file (.mid).', upload_to='midi_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]