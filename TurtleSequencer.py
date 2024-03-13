import turtle
from turtle import Turtle
#from turtle import goto
from pathlib import Path
from random import randint
from PIL import Image, UnidentifiedImageError



iscomputer = False
try:
    #DO NOT REMOVE THIS TRY-CATCH, IT IS USED TO CHECK IF YOU ARE USING THE PYTHONISTA APP OR NOT
    import scene
except ModuleNotFoundError: iscomputer = True

if iscomputer: dimensions = 355, 357; print('current device is a computer, loading computer dimensions')
else: dimensions = 147, 147; print('current device isn\'t a computer, loading pocket device dimensions')

imgscalefactor = 5



def removeitems(list: list, items: list | tuple):
    out = []
    for i in list:
        if i not in items: out.append(i)
    return out





turtle.hideturtle()
Turt = Turtle('classic', 1000, True)
screen = Turt.getscreen()
screen.colormode(255)
#screen.screensize()
#print(screen.window_width() / 2, screen.window_height() / 2)
#print(screen.canvwidth, screen.canvheight)



if not Path('TSin.txt').exists():
    with open('TSin.txt', 'xt') as fir: fir.write('')
Turt.goto(0,0)



test1 = [(100,0), (100,100), (-100,100), (-100,-100), (100,-100), (100,0)]

test2 = [(100,0), (-100,0), (0,0), (0,100), (0,-100), (0,0), (-100,-100), (100,100), (0,0), (100,-100), (-100,100), (0,0)]

test3 = [(225, 500), (65, 185), (390, 65), (-10, 550), (-10, -10), (290, 255), (225, 285), (310, 400), (425, 215), (165, 480), (55, 135)]

test4 = [(225, 265), (335, 145), (460, 345), (150, 475), (35, 190)]


def no_hardcode_found(command_name: str, *empty): print(f'no command "{command_name}" found')

class hardcoded:
    def gethardcode(hardcodename):
        gottencommand = getattr(hardcoded, hardcodename, no_hardcode_found)
        gottencommand()

    def boxes():
        Turt.color('white')
        Turt.goto(4, -4)
        Turt.color('black')
        Turt.goto(-24, -4)
        Turt.goto(-24, 24)
        Turt.goto(4, 24)
        Turt.goto(4, -4)
        Turt.color('white')
        Turt.goto(64, 54)
        Turt.color('black')
        Turt.goto(64, 94)
        Turt.goto(104, 94)
        Turt.goto(104, 54)
        Turt.goto(64, 54)
        Turt.color('white')
        Turt.goto(34, -54)
        Turt.color('black')
        Turt.goto(14, -54)
        Turt.goto(-4, -74)
        Turt.goto(-4, -94)
        Turt.goto(14, -114)
        Turt.goto(34, -114)
        Turt.goto(54, -94)
        Turt.goto(54, -74)
        Turt.goto(34, -54)
        Turt.color('white')
        Turt.goto(-114, -34)
        Turt.color('black')
        Turt.goto(-184, -34)
        Turt.goto(-184, -104)
        Turt.goto(-114, -104)
        Turt.goto(-114, -34)
        Turt.hideturtle()


    def box3d():
        Turt.goto(4, -4)
        Turt.goto(134, -4)
        Turt.goto(134, -94)
        Turt.goto(4, -94)
        Turt.goto(4, -4)
        Turt.goto(64, -4)
        Turt.goto(64, -94)
        Turt.hideturtle()

    def mouseface():
        Turt.goto(31, -210)
        Turt.goto(141, -59)
        Turt.goto(137, 138)
        Turt.goto(0, 217)
        Turt.goto(-117, 144)
        Turt.goto(-120, -60)
        Turt.goto(31, -212)
        Turt.color('white')
        Turt.goto(-30, -94)
        Turt.color('black')
        Turt.goto(72, -95)
        Turt.goto(70, -27)
        Turt.goto(-34, -30)
        Turt.goto(-30, -94)
        Turt.color('white')
        Turt.goto(-64, -92)
        Turt.color('black')
        Turt.color('white')
        Turt.goto(-68, 12)
        Turt.color('black')
        Turt.color('white')
        Turt.goto(-43, 57)
        Turt.color('black')
        Turt.goto(-2, 60)
        Turt.goto(-2, 114)
        Turt.goto(-52, 114)
        Turt.goto(-44, 58)
        Turt.color('white')
        Turt.goto(4, 34)
        Turt.color('black')
        Turt.goto(-15, -2)
        Turt.goto(28, -3)
        Turt.goto(5, 35)
        Turt.color('white')
        Turt.goto(38, 56)
        Turt.color('black')
        Turt.goto(39, 115)
        Turt.goto(87, 116)
        Turt.goto(87, 54)
        Turt.goto(38, 56)
        Turt.hideturtle()


    def rect3d():
        Turt.color('white')
        Turt.goto(100, 100)
        Turt.color('black')
        Turt.goto(100, 100)
        Turt.goto(70, 100)
        Turt.goto(70, 0)
        Turt.goto(70, 0)
        Turt.goto(100, 0)
        Turt.goto(100, 100)
        Turt.goto(30, 100)
        Turt.goto(30, 0)
        Turt.goto(70, 0)
        Turt.hideturtle()

hardcodes = removeitems(list(vars(hardcoded).keys()), ('__module__', 'gethardcode', '__dict__', '__weakref__', '__doc__'))



clog = []
def log(data): clog.append(data)


def totlist(rawlist: list):
    #print('rawlist:' + str(rawlist))
    final = []
    for r in rawlist:
        sr = r.split(',')
        if len(sr) >= 3: tr = int(sr[0]), int(sr[1]), sr[2]
        else: tr = int(sr[0]), int(sr[1])
        final.append(tr)
        #print('totlist:', r)
    #print(final)
    return final

def totl(list: list):
    ostr = ''
    for l in list:
        tstr = f'{l[0]},{l[1]}'
        ostr = ostr + tstr + '/'
    if ostr[-1]: ostr = ostr.removesuffix('/')
    return ostr


def sequence(tlist: list | tuple, shouldhardcode: bool, shouldhide: bool):
    if shouldhide: Turt.hideturtle()
    out = ''
    if shouldhardcode:
        for t in tlist:
            if len(t) >= 3: out = f'{out}Turt.color(\'{t[2]}\')\nTurt.goto({t[0]}, {t[1]})\nTurt.color(\'black\')\n'
            else: out = f'{out}Turt.goto{t}\n'
        out = f'{out}Turt.hideturtle()'
        print(out)
    else:
        for t in tlist:
            if len(t) >= 3:
                Turt.color(str(t[2]))
                Turt.goto(t[0], t[1])
                print(f'moved Turt to ({t[0]}, {t[1]}) as "{t[2]}"')
                Turt.color('black')
            else:
                Turt.goto(t[0], t[1])
                print(f'moved Turt to {t}')


def getfile(file: str | None):
    if file == None:
        with open('TSin.txt', 'rt') as fin: return fin.read()
    else:
        with open(f'drawings/{file}.txt', 'rt') as fin: return fin.read()

def getfileall(file: str | None):
    with open(f'{file}', 'rt') as fin: return fin.read()


def getlogs():
    global clog
    fout = ''
    for lo in clog:
        fout = fout + '/' + lo
    print(fout)


shouldturn = True
def randtur():
    Turt.speed(0)
    rinp = input('how many times?> ')
    for _ in range(int(rinp)):
        xy = randint(dimensions[0], dimensions[1]), randint(dimensions[0], dimensions[1])
        if shouldturn:
            rol = randint(0, 1)
            if rol == 0: Turt.right(randint(0, 360))
            else: Turt.left(randint(0, 360))
        Turt.goto(xy[0], xy[1])
        print(f'moved Turt to {xy}')
    Turt.setheading(180)
    Turt.speed(6)


def moveto(x: int | tuple[int, int], y: int | None = None):
    Turt.pencolor(255, 255, 255)
    if type(x) == tuple and type(y) == None: Turt.goto(x)
    else: Turt.goto(x, y)
    Turt.pencolor(0, 0, 0)


def drawpixel(color: tuple[int, int, int] | tuple[int, int, int, int]):
    if len(color) < 3: print(f'unable to read color "{color}", too small'); return
    try: trans = color[3]
    except: trans = 255
    clear = False
    if trans <= 0: clear = True; Turt.pencolor(255, 255, 255)
    else: Turt.color(color[0], color[1], color[2])
    if clear:
        Turt.setheading(0)
        Turt.forward(imgscalefactor)
        return
    Turt.begin_fill()
    Turt.setheading(0)
    Turt.forward(imgscalefactor)
    Turt.setheading(90)
    Turt.forward(imgscalefactor)
    Turt.setheading(180)
    Turt.forward(imgscalefactor)
    Turt.setheading(270)
    Turt.forward(imgscalefactor)
    Turt.setheading(0)
    Turt.forward(imgscalefactor)
    Turt.end_fill()



def multisquen(list: list | tuple, shouldhardcode: bool, shouldhide: bool):
    for line in list:
        if not line.startswith('--') and line != '':
            ln = line.split('--')[0].split('/')
            sequence(totlist(ln), shouldhardcode, shouldhide)



def TS():
    print('the cursor\'s name is Turt')
    print('instructions should be in the format of "x,y/x,-y,[color]/-x,y,[color]"')
    print('to get instructions from a file, type "file [filename, not including extension]"')
    print('to see Turt\'s position, type "pos"')
    print('to see Turt\'s angle, type "angle"')
    print('to hide Turt, type "hide"')
    print('to show Turt, type "show"')
    print('to undo, type "undo"')
    print('to clear all of Turt\'s beautiful drawings(you monster), type "clear"')
    print('to reset everything to AS IT WAS, type "reset"')
    print('to make Turt go batcrap insane and do whatever the heck he wants, type "random"')
    #print('to draw a preset, type "draw [preset number]", currently availible presets: 1, ')

    pointer = '> '
    hardcode = False
    hide = False
    prev = '' #image Turt(16).png

    running = True
    while running:
        tsinp = input(pointer).strip()
        if tsinp != 'prev': prev = tsinp

        if tsinp == 'prev' and prev.strip() != '': tsinp = prev

        if tsinp == 'exit' or tsinp == 'quit': running = False; break

        elif tsinp == 'clear': Turt.clear(); print('cleared all drawings')

        elif tsinp == 'reset': Turt.goto(0,0); Turt.clear(); print('reset everything')

        #elif 'image' in tsinp: #Turt.register_shape(tsinp.split(' ')[1])

        #elif tsinp == 'draw 1': Turt.shape('Greeben-flat.gif')#Turt.shape(tsinp.split(' ')[1])

        elif tsinp == 'log' or tsinp == 'logs': getlogs()

        elif tsinp == 'show': Turt.showturtle(); print('Turt shown')

        elif tsinp == 'hide': Turt.hideturtle(); print('Turt hidden')

        elif tsinp == 'undo': Turt.undo(); print('undid draw')

        elif tsinp == 'pos': print(f'Turt{Turt.pos()}')

        elif tsinp == 'angle': print(f'Turt({Turt.heading()})')

        elif tsinp == 'random': randtur()

        elif tsinp == 'test1': sequence(test1)

        elif tsinp == 'test2': sequence(test2)

        elif tsinp == 'test3': sequence(test3)

        elif tsinp == 'test4': sequence(test4)

        elif tsinp.startswith('image '):
            tsinp = tsinp.removeprefix('image ')
            if not Path(tsinp).exists(): print(f'file "{tsinp}" does not exist'); continue
            try:
                img = Image.open(tsinp)
            except UnidentifiedImageError: print(f'file "{tsinp}" is not a valid image file'); continue
            imgsize = img.size
            #imgsizescaled = imgsize[0] * imgscalefactor, imgsize[1] * imgscalefactor
            #if imgsizescaled[0] > dimensions[0] * 2 or imgsizescaled[1] > dimensions[1] * 2: print(f'file "{tsinp}" is too large'); continue
            startpos = -200, 200
            moveto(startpos)
            prevspeed = Turt.speed()
            Turt.speed(0)
            for col in range(imgsize[0]):
                for row in range(imgsize[0]):
                    pixel = img.getpixel((row, col))
                    #print(f'drawing pixel (col:{col},row:{row}) with color {pixel}')
                    drawpixel(pixel)
                Turt.setheading(270)
                Turt.forward(1)
                moveto(startpos[0], startpos[1] - imgscalefactor * (col + 1))
            Turt.speed(prevspeed)

        elif tsinp.startswith('dimensions'):
            if tsinp == 'dimensions': print(dimensions)
            #elif tsinp.startswith('dimensions '):
            #    try:
            #        di = tsinp.removeprefix('dimensions ').strip().split(', ')
            #        dimensions = int(di[0]), int(di[1])
            #    except ValueError: print(print(f'"{tsinp.removeprefix("dimensions ").strip()}" is not valid'))

        elif tsinp.startswith('hardcoded '): hardcoded.gethardcode(tsinp.removeprefix('hardcoded '))

        elif tsinp.startswith('speed'):
            #print(len(tsinp.split(' ')))
            if tsinp == 'speed': print(f'Turt({Turt.speed()})')
            elif tsinp.removeprefix('speed ').strip() == 'reset': Turt.speed(3); print('reset Turt\'s speed to normal')
            else:
                try:
                    Turt.speed(int(tsinp.strip().removeprefix('speed ').strip()))
                    print(f'set Turt\'s speed to {tsinp.removeprefix("speed ").strip()}')
                except ValueError: print(print(f'"{tsinp.removeprefix("speed ").strip()}" is not valid'))

        else:
            if tsinp.startswith(('file ', 'run ')):
                tsinp = tsinp.removeprefix('file ').removeprefix('run ')
                if tsinp.strip() == '':
                    tsinp = getfile(None)
                    tsfile = tsinp.split('\n')
                    multisquen(tsfile, hardcode, hide)
                else:
                    tsinp = tsinp.split(' ')
                    path = tsinp.pop(0)
                    hardcode = 'hardcode' in tsinp
                    hide = 'hide' in tsinp
                    if path == 'all':
                        for file in Path('./drawings/').iterdir():
                            print(f'====CURRENTFILE: {str(file)}====')
                            multisquen(getfileall(file).split('\n'), hardcode, hide)
                    else:
                        tsinp = getfile(path)
                        tsfile = tsinp.split('\n')
                        multisquen(tsfile, hardcode, hide)
                
            else:
                rlist = tsinp.split('/')
                sequence(totlist(rlist), hardcode, hide)
        log(tsinp)


TS()
#Greeben-flat.png









#0,100/20,100/20,110/50,110/60,100/60,90/70,90/70,50/60,50/60,30/50,30/50,20/40,20/40,0/30,0/30,-10/20,-10/20,-20/10,-20/10,-30






#35,165/145,280/5,335/105,455/220,280/105,160/40,65/15,460/35,510/


#-10,130/-10,40/50,255/-5,325/55,325/110,250/150,175/150,85/75,85/75,110/45,170/45,200/80,230/110,185/110,110/75,320/75,400/75,450/30,450/30,450/30,395/30,360/30,310/30,260


#0,-162/-6,-150/12,-150/-34,-134/-86,-110/-162,-90/-22,-54/0,32/20,-54/40,-134/92,-110/148,-90/20,-54


#-148,148/-151,-81/69,-81/69,154/-34,115/-73,79/-40,52/-10,82/42,16/42,-42/-121,-42/-121,16/-40,16/-40,-45


#0,0/-112,-24/-118,-141/15,-192/66,-57/0,1/78,103/-88,199/-199,76/-115,-24/-202,79/-304,10/-304,-123/-253,-177/-118,-144/-253,-177/-253,-282/-106,-297/12,-279/15,-192/249,-192/249,22/123,22/123,-189/150,-129/174,-141/198,-141/219,-117/219,-48/231,-24/210,-12/189,-30/219,-48/156,-48/141,-24/159,-6/171,-24/156,-45


#0,-168/-145,-72/-184,43/-109,157/66,172/165,82/120,-39/0,-168/165,82/51,1/21,-30/-34,-30/-58,-3/-37,0/-19,-15/15,-12/33,10/51,1/51,88/27,115/6,100/6,85/21,79/51,88/21,79/-40,76/-70,76/-88,106/-64,124/-40,109/-40,79





#0,100/-80,40/-25,0/0,0/0,100/80,40/25,0/0,0/-13,0/0,-100/13,0/0,0
#0,75/-7,75/-7,70/0,70/0,75/7,75/7,70/0,70/0,0
#0,65/-10,65/-10,60/0,60/0,65/10,65/10,60/0,60
#0,55/-14,55/-14,50/0,50/0,55/14,55/14,50/0,50
#0,45/-14,45/-14,40/0,40/0,45/14,45/14,40/0,40
#0,35/-24,35/-24,30/0,30/0,35/24,35/24,30/0,30
#0,25/-36,25/-36,20/0,20/0,25/36,25/36,20/0,20
#0,-20/0,0
