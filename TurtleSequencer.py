import turtle
from turtle import Turtle
#from turtle import goto
from pathlib import Path
from random import randint
import struct
turtle.hideturtle()


Turt = Turtle('classic', 1000, True)
#Turt.speed(1)
#turtle.register_shape('Greeben-flat.gif')




if not Path('TSin.txt').exists():
    with open('TSin.txt', 'xt') as fir: fir.write('')
Turt.goto(0,0)
#screen = Screen()
#screen.screensize(800, 800)

test1 = [(100,0), (100,100), (-100,100), (-100,-100), (100,-100), (100,0)]

test2 = [(100,0), (-100,0), (0,0), (0,100), (0,-100), (0,0), (-100,-100), (100,100), (0,0), (100,-100), (-100,100), (0,0)]

test3 = [(225, 500), (65, 185), (390, 65), (-10, 550), (-10, -10), (290, 255), (225, 285), (310, 400), (425, 215), (165, 480), (55, 135)]

test4 = [(225, 265), (335, 145), (460, 345), (150, 475), (35, 190)]


#def Turty():

def get_image_info(data):
    if is_png(data):
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w)
        height = int(h)
    else: print('error: not a png image')#raise Exception('not a png image')
    return width, height

def is_png(data):
    return (data[:8] == '\211PNG\r\n\032\n'and (data[12:16] == 'IHDR'))



REPEAT = False


clog = []
def log(data): clog.append(data)


def totlist(rawlist: list):
    final = []
    for r in rawlist:
        sr = r.split(',')
        tr = int(sr[0]), int(sr[1])
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


def sequence(tlist: list | tuple):
    for t in tlist: Turt.goto(t[0], t[1]); print(f'moved Turt to {t}')


def getfile(file: str | None):
    if file == None:
        with open('TSin.txt', 'rt') as fin: return fin.read()
    else:
        with open(f'drawings/{file}.txt', 'rt') as fin: return fin.read()

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
    for q in range(int(rinp)):
        xy = randint(-147, 147), randint(-147, 147)
        if shouldturn:
            rol = randint(0, 1)
            if rol == 0: Turt.right(randint(0, 360))
            else: Turt.left(randint(0, 360))
        Turt.goto(xy[0], xy[1])
    Turt.speed(6)


def turny():
    Turt.left(75)

def TS():
    print('the cursor\'s name is Turt')
    print('instructions should be in the format of "x,y/x,-y/-x,y"')
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
    lcheck = []
    multiline = False
    while True:
        tsinp = input(pointer)
        #print(tsinp)
        if tsinp == 'exit' or tsinp == 'quit': break
        elif tsinp == 'clear': Turt.clear(); print('cleared all drawings')
        elif tsinp == 'reset': Turt.goto(0,0); Turt.clear(); print('reset everything')
        #elif 'image' in tsinp: #Turt.register_shape(tsinp.split(' ')[1])
        #elif tsinp == 'draw 1': Turt.shape('Greeben-flat.gif')#Turt.shape(tsinp.split(' ')[1])
        elif tsinp == 'log' or tsinp == 'logs': getlogs()
        elif tsinp == 'show': Turt.showturtle(); print('Turt shown')
        elif tsinp == 'hide': Turt.hideturtle(); print('Turt hidden')
        elif tsinp == 'undo': Turt.undo(); print('undid draw')
        elif tsinp == 'pos':  print(f'Turt{Turt.pos()}')
        elif tsinp == 'angle':  print(f'Turt({Turt.heading()})')
        elif tsinp.split(' ')[0] == 'speed':
            #print(len(tsinp.split(' ')))
            if len(tsinp.split(' ')) < 2: print(f'Turt({Turt.speed()})')
            elif tsinp.split(' ')[1] == 'reset' or tsinp.split(' ')[1] == 'reset': Turt.speed(3); print('reset Turt\'s speed to normal')
            else: Turt.speed(int(tsinp.split(' ')[1])); print(f'set Turt\'s speed to {tsinp.split(" ")[1]}')
        elif tsinp == 'random': randtur()
        else:
            #print('got to the first else!')
            if tsinp == 'test1': sequence(test1)
            elif tsinp == 'test2': sequence(test2)
            elif tsinp == 'test3': sequence(test3)
            elif tsinp == 'test4': sequence(test4)
            else:
                #print('got to the second else!')
                if tsinp.split(' ')[0] == 'file' or tsinp.split(' ')[0] == 'run':
                    if len(tsinp.split(' ')) >= 2:
                        tsinp = getfile(tsinp.split(' ')[1])
                        lcheck = tsinp.split('\n')
                        if len(lcheck) >= 2: multiline = True
                    else:
                        tsinp = getfile(None)
                        lcheck = tsinp.split('\n')
                        if len(lcheck) >= 2: multiline = True
                rlist = tsinp.split('/')
                #print(rlist)
                if multiline:
                    for line in lcheck:
                        if not '--' in line and line != '':
                            ln = line.split('/') 
                            sequence(totlist(ln))
                else: sequence(totlist(rlist))
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