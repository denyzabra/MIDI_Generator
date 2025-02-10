from midiutil import MIDIFile


midi = MIDIFile(1)  
track = 0  
time = 0  
tempo = 120  
midi.addTempo(track, time, tempo)


chord_map = {
    "G": [55, 59, 62],    # G Major
    "G7": [55, 58, 62],   # G7
    "C": [48, 52, 55],    # C Major
    "C7": [48, 52, 55, 58],  # C7
    "Am": [57, 60, 64],   # A minor
    "D7": [50, 54, 57, 60],  # D7
    "Em": [52, 55, 59],   # E minor
    "B7": [47, 51, 54, 58],  # B7
    "F": [53, 57, 60],    # F Major
}


progression = [
    "G", "G7", "C", "C7",
    "G", "G7", "Am", "D7",
    "G", "G7", "C", "C7",

    "Em", "B7", "C", "G",
    "Em", "B7", "C", "G",

    "G", "G7", "C", "C7",
    "G", "G7", "Am", "D7",
    "G", "G7", "C", "C7",
    "G", "G7", "Am", "D7",

    "Em", "B7", "C", "G",
    "Em", "B7", "C", "G",

    "Am", "F", "G", "C",
    "Am", "F", "G", "C",
    "Am", "F", "G", "C",

    "G", "G7", "C", "C7",
    "G", "G7", "C", "C7",
]


channel = 0  
volume = 100  
duration = 2  

for chord in progression:
    notes = chord_map.get(chord, [])
    for note in notes:
        midi.addNote(track, channel, note, time, duration, volume)
    time += duration


with open("chord_progression.mid", "wb") as file:
    midi.writeFile(file)

print("MIDI file successfully created: chord_progression.mid")

