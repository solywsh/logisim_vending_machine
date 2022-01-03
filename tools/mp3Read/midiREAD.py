import mido
import queue




def main():
    Note2Hz = [28, 29, 31, 33, 35, 37, 39, 41, 44, 46, 49, 52, 55, 58, 62, 65, 69, 73, 78, 82, 87, 93, 98, 104, 110,
               117,
               124, 131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392,
               415,
               440, 466, 494, 523, 554, 587, 622, 659, 699, 740, 784, 831, 880, 932, 988, 1046, 1109, 1175, 1245, 1319,
               1397, 1480, 1568, 1661, 1760, 1865, 1976, 2093, 2218, 2349, 2489, 2637, 2793, 2960, 3136, 3322, 3520,
               3729,
               3951, 4186]

    # path = input()
    path = "FlyMeToTheMoon.mid"
    mid = mido.MidiFile(path)
    right = mid.tracks[1]
    SHz = 50
    Hz = mid.ticks_per_beat * 2
    with open(path[:-3] + 'hex', 'w') as f:
        f.write('v2.0 raw\n')
        q = queue.Queue()
        l = 0
        t = 0
        last = 0
        s = set()
        for msg in right:
            t += msg.time * SHz // Hz
            if msg.type == 'note_on' or msg.type == 'note_off':
                if msg.note not in s:
                    s.add(msg.note)
                    q.put(t)
                else:
                    s -= {msg.note}
                    begin = q.get()
                    for i in range(last, begin):
                        f.write('00000000 ')
                        l += 1
                    for i in range(begin, t):
                        f.write('%08x ' % Note2Hz[msg.note - 21])
                        l += 1
                    last = t
        f.write('\n%08x' % l)

if __name__ == "__main__":
    main()
