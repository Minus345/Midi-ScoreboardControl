import sys

import mido

url = ""
event = 0
heat = 0


def parse_args():
    global url, event, heat
    if len(sys.argv) > 1:
        url = sys.argv[1]
    if len(sys.argv) > 2:
        event = int(sys.argv[2])
    if len(sys.argv) > 3:
        heat = int(sys.argv[3])


def search_midi():
    print("Select midi source:")
    midi_source_list = []
    source_counter = 0
    for source in mido.get_input_names():
        print(str(source_counter) + " : " + source)
        midi_source_list.append(source)
        source_counter += 1
    print("Typ input number for midi source:")
    line = input()
    number = 0
    try:
        number = int(line)
    except ValueError:
        print("Invalid number")
        sys.exit(0)

    if number < 0 or number > len(midi_source_list):
        print("Invalid number")
        sys.exit(0)
    print("Start midi input with source: " + midi_source_list[number])

    with mido.open_input(midi_source_list[number]) as inport:
        for msg in inport:
            print(msg)


if __name__ == '__main__':
    parse_args()
    print("Midi-ScoreboardControl")
    print("url: " + url)
    print("event: " + str(event))
    print("heat: " + str(heat))
    search_midi()
