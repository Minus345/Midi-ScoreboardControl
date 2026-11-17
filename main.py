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
    mido.get_input_names()
    with mido.open_input() as inport:
        for msg in inport:
            print(msg)


if __name__ == '__main__':
    parse_args()
    print("Midi-ScoreboardControl")
    print("url: " + url)
    print("event: " + str(event))
    print("heat: " + str(heat))
    search_midi()
