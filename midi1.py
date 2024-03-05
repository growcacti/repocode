import mido
import time
from mido import Message
from pyFluidSynth.fluidsynth import Fluidsynth

# Initialize fluidsynth synthesizer
fs = Fluidsynth()
fs.start(driver="alsa")  # Use 'coreaudio' for Mac

# Use a SoundFont (assumes you have a .sf2 file)
sfont_id = fs.sfload("example.sf2")  # replace with your .sf2 file
fs.program_select(0, sfont_id, 0, 0)

# Open a MIDI input port
inport = mido.open_input("Your MIDI Device")  # replace with your MIDI device

print("Listening for MIDI messages...")

# Loop to listen for MIDI messages
try:
    for msg in inport:
        # We're only interested in note-on or note-off messages
        if msg.type == "note_on" or msg.type == "note_off":
            # Play note using fluidsynth
            if msg.type == "note_on":
                fs.noteon(0, msg.note, msg.velocity)
            else:
                fs.noteoff(0, msg.note)

        # Other types of messages are ignored
        else:
            continue

except KeyboardInterrupt:
    # Clean up
    print("Closing MIDI input...")
    inport.close()

print("Done.")
