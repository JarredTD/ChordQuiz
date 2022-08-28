import json
from random import randint

with open("Chords\\Chords.txt", 'r') as chord_file:
    chord_list = chord_file.read()

chord_list = chord_list.splitlines()
while len(chord_list) > 0:
    i = randint(0, len(chord_list)-1)

    input(chord_list[i])
    chord_list.pop(i)

input('Done')
