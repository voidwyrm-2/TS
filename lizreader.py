'''
with open('Spearzard.liz', 'rb') as f: lizbytes = f.read()

lbs = str(lizbytes)

lbh = lizbytes.hex()

with open('Spearzard-str.nc', 'wt') as strout: strout.write(lbs)

with open('Spearzard-hex.nc', 'wt') as hexout: hexout.write(lbh)
'''


def hextorgb(hex: str, printit: bool = False):
    #h = input('Enter hex: ').lstrip('#')
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    #if printit: print('RGB =', rgb)
    return rgb



def to2dlist(list: list, xy: tuple[int, int]):
    #if len(list) < xy[0] * xy[1]: print('given list too small'); return
    out = []
    o = []
    col = 0
    row = 0
    for l in list:
        if col >= xy[1]: row = 0; out.append(o); break
        if row == xy[0]: row = 0; out.append(o); o = []
        o.append(l)
        #print('row', str(row) + ';')
        row += 1
        col += 1
    return out


def liztoimage(path: str):

    with open(path, 'rb') as bytesin: hex = bytesin.read().hex()

    hexlen3 = (len(hex) // 6) * 6
    hl2 = (hexlen3 - 1) // 2
    #print(hexlen3)
    #print(hl2)

    out = []
    o = ''
    c = 0
    h = 0
    for char in hex:
        if c >= hexlen3: break
        if h == 6: out.append(o); h = 0; o = ''
        o += char
        h += 1
        c += 1

    rgbout = []

    for i in out:
        rgb = hextorgb(i)
        rgbout.append((rgb[0], rgb[1], rgb[2], 255))

    out2d = to2dlist(rgbout, (125, 600))

    return out2d