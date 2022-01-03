paths = ['Cristina.hex', 'for elise.hex', 'Полет шмеля.hex']

with open('music.hex', 'w') as f:
    f.write('v2.0 raw\n')
    empty = ''
    for i in range(64):
        empty += '00000000 '
    empty += '\n'
    p = 0
    position = []
    x = []
    for path in paths:
        lines = open(path, 'r').readlines()
        position.append(p)
        l = int(lines[-1], base = 16)
        l += 64+4
        x.append('%08x ' % (p+4*4))
        x.append('%08x ' % (p+l*4))
        x.append(None)
        x.append('%08x \n' % (p+l*4))
        x.append(lines[1])
        x.append(empty)
        p += l * 4
    for i in range(len(paths)):
        x[6 * i + 2] = '%08x ' % position[i-1]
    x[6*2+3] = '00000000 \n'
    for s in x:
        f.write(s)

