from mido import Message, MidiFile, MidiTrack


# Function to save a sequence of notes as a MIDI file
def save_to_midi(sequence, filename):
    midi = MidiFile()

    # Create a new MIDI track
    track = MidiTrack()

    # Add the track to the MIDI file
    midi.tracks.append(track)

    # Add notes from the sequence to the track
    for note in sequence:
        # Add a "note on" message to start playing the note
        track.append(Message('note_on', note=note, velocity=64, time=200))
        # Add a "note off" message to stop playing the note
        track.append(Message('note_off', note=note, velocity=64, time=200))

    # Save the MIDI file to the specified filename
    midi.save(filename)
    print(f"Saved MIDI file: {filename}")


