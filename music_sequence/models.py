from django.db import models


class MidiFile(models.Model):
    title = models.CharField(max_length=255, help_text="Enter a descriptive title for the MIDI file.")
    fitness = models.CharField(max_length=200, default='')
    sequence = models.CharField(max_length=200, default='')
    audio = models.FileField(upload_to='melody/', help_text="Upload a valid MIDI file (.mid).")

    def __str__(self):
        return self.title
