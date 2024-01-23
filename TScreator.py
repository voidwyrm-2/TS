import pygame








def limit(input, max):
    if input > max: return max
    return input

def limitmin(input, min):
    if input < min: return min
    return input



def log(data):
    with open('LOG.txt', 'at') as flog: flog.write(str(data) + '\n')



colors = [
    'black',
    'white',
    'red',
    'blue',
    'green',
    'purple',
    'cyan',
    'yellow',
    'orange',
    'pink'
]

colorvals = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0),
    'purple': (255, 0, 255),
    'cyan': (0, 255, 255),
    'yellow': (255, 255, 0),
    'orange': (255, 131, 0),
    'pink': (255, 191, 191)
}



# initialize game
pygame.init()

# creating a screen
windratio = 356*2, 356*2
screen = pygame.display.set_mode(windratio)  # passing width and height
screen.fill("black")
pygame.display.flip()
# title and icon
pygame.display.set_caption("TSCreator")
#icon = pygame.image.load('')
#pygame.display.set_icon(icon)
#pygame.draw.rect()
clock = pygame.time.Clock()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

savetofile = True
pixelmode = False

SHOWACTUALCOORDS = False

plinitxy = windratio[0] // 2, windratio[1] // 2

if pixelmode: plinitxy = 360, 360

wps = []
ismoving = True
plicon = pygame.image.load('Turt.png')
plX = plinitxy[0]
plY = plinitxy[1]
speed = 3
changedX = 0
changedY = 0
def player(px, py, icon): pygame.draw.circle(screen, (0, 0, 255), (px, py), 7)


mouseX = 0
mouseY = 0
mouseIsPressed = False

colorindex = 0


def reversex(num: int, max: int):
    nums = []
    for n in range(max - 1):
        if n != 0: nums.append(n)
    return -nums[limitmin(num - 1, -(len(nums) - 1))]

def reversey(num: int, max: int):
    nums = []
    for n in range(max):
        if n != 0: nums.append(n)
    #log(f'Y:{nums}')
        #print(f'{num}, {n}({max})')
    return -nums[limitmin(num - 1, -(len(nums) - 1))]



def fixY(Ycoord: int): return -Ycoord


def convertx(coord: int, ratio: int):
    hratio = (ratio // 2)
    #print(hratio)
    if coord < hratio: return reversex(-coord, hratio)
    if coord >= hratio: return coord - hratio

def converty(coord: int, ratio: int):
    hratio = (ratio // 2)
    #print(hratio)
    if coord < hratio: return reversey(-coord, hratio) #coord // 2
    if coord >= hratio: return coord - hratio

def showWpoints(x, y):
    wp = mainfont.render(f'Waypoints: {len(wps)}', True, (255, 255, 255))
    screen.blit(wp, (x, y))

def showcoords(x, y):
    co = mainfont.render(f'plX:{convertx(plX, windratio[0])},plY:{fixY(converty(plY, windratio[1]))}', True, (255, 255, 255))
    #co = mainfont.render(f'plX:{plX},plY:{plY}', True, (255, 255, 255))
    screen.blit(co, (x, y))


def showcolor(x, y):
    curco = mainfont.render(f'current color:', True, (255, 255, 255)); screen.blit(curco, (x, y))
    dacolor = mainfont.render(f'{colors[colorindex]}', True, colorvals[colors[colorindex]]); screen.blit(dacolor, (x, y + 35))


def showtruecoords(x, y):
    truco = mainfont.render(f'plX:{plX},plY:{plY}', True, (255, 255, 255))
    #co = mainfont.render(f'plX:{plX},plY:{plY}', True, (255, 255, 255))
    screen.blit(truco, (x, y))


def placeWaypoints():
    wpsize = 5
    if pixelmode: wpsize = 2
    for w in wps:
        if len(w) >= 3: pygame.draw.circle(screen, colorvals[w[2]], (w[0], w[1]), wpsize)
        else: pygame.draw.circle(screen, (50, 50, 50), (w[0], w[1]), wpsize)

def drawWPlines():
    for p in range(len(wps)):
        p1 = wps[limit(p, len(wps) - 1)]
        p2 = wps[limit(p + 1, len(wps) - 1)]
        if len(p2) >= 3: pygame.draw.line(screen, colorvals[p2[2]], (p1[0], p1[1]), (p2[0], p2[1]), 3)
        else: pygame.draw.line(screen, (50, 50, 50), (p1[0], p1[1]), (p2[0], p2[1]), 3)


def drawsquare(radius):
    global plX
    global plY
    global wps
    wps.append((plX + radius, plY + radius))
    wps.append((plX - radius, plY + radius))
    wps.append((plX - radius, plY - radius))
    wps.append((plX + radius, plY - radius))
    wps.append((plX + radius, plY + radius))


def drawcircle(radius, points):
    global plX
    global plY
    global wps
    wps.append((plX + radius, plY + radius))
    wps.append((plX + radius, plY + (radius // 2)))
    wps.append((plX - radius, plY + radius))
    wps.append((plX - radius, plY - radius))
    wps.append((plX + radius, plY - radius))
    wps.append((plX + radius, plY + radius))
    #for cp in range(points):
        #if cp < pointsq + 1: wps.append((plX + radius, plY + radius))
        #if cp > pointsq + 1 and cp < (pointsq * 2) + 1: wps.append((plX + radius, plY + radius))
        #if cp > pointsq + 1 and cp < (pointsq * 3) + 1: wps.append((plX + radius, plY + radius))
        #if cp > pointsq + 1 and cp < (pointsq * 4) + 1: wps.append((plX + radius, plY + radius))
            

def showcursorpos(x, y):
    global mouseX
    global mouseY
    cp = mainfont.render(f'mouse_pos:{mouseX},{mouseY}', True, (255, 255, 255))
    screen.blit(cp, (x, y))


def drawpixelgrid():
    stepX = 0
    stepY = 0
    for li1 in range(windratio[1]):
        if li1 == stepX:
            pygame.draw.line(screen, (100, 100, 100), (0, stepX), (windratio[0], stepX))
            stepX += 10

    for li2 in range(windratio[0]):
        if li2 == stepY:
            pygame.draw.line(screen, (100, 100, 100), (stepY, 0), (stepY, windratio[1]))
            stepY += 10




def instructs(wayp: list):
    out = ''
    if len(wayp) <= 0: return
    for co in wayp:
        if len(co) >= 3: ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))},{co[2]}'
        else: ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))}'
        out = out + f'{ins}/'
    #if out[-1] == '/': del out[-1]
    return out.removesuffix('/')


def save(turstructs: str):
    if savetofile:
        savename = input('please type a name\n')
        with open(f'drawings/{savename}.txt', 'xt') as savefile: savefile.write(turstructs)
        print('TS instructions generated')
    else: print(turstructs)




running = True
while running:
    screen.fill((0, 0, 0))  # background
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
            #print("you preesed a key")
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: running = False; break

            if event.key == pygame.K_RETURN:
                if colorindex != 0: wps.append((plX, plY, colors[colorindex]))
                else: wps.append((plX, plY))

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if pixelmode: plX -= 10
                else: changedX = -speed#; ismoving = True

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if pixelmode: plX += 10
                else: changedX = speed#; ismoving = True

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if pixelmode: plY -= 10
                else: changedY = -speed#; ismoving = True

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if pixelmode: plY += 10
                else: changedY = speed#; ismoving = True

            if event.key == pygame.K_o:
                if len(wps) >= 1: del wps[-1]
                
            if event.key == pygame.K_c: wps.clear()

            if event.key == pygame.K_x:
                plX = windratio[0] // 2
                if pixelmode: plX += 4

            if event.key == pygame.K_y:
                plY = windratio[1] // 2
                if pixelmode: plY += 4

            if event.key == pygame.K_z:
                plX = windratio[0] // 2; plY = windratio[0] // 2
                if pixelmode: plX += 4; plY += 4

            if event.key == pygame.K_r:
                plX = windratio[0] // 2; plY = windratio[0] // 2
                if pixelmode: plX += 4; plY += 4
                wps.clear()

            if event.key == pygame.K_p: save(instructs(wps))

            if event.key == pygame.K_1: drawsquare(20)#; print(wps)

            if event.key == pygame.K_2: drawcircle(20, 20); print(wps)

            if event.key == pygame.K_0:
                if pixelmode: wps.append(((windratio[0] // 2) + 4,(windratio[1] // 2) + 4))
                else: wps.append((windratio[0] // 2,windratio[1] // 2))
            
            if event.key == pygame.K_LEFTBRACKET and colorindex > 0: colorindex -= 1
            if event.key == pygame.K_RIGHTBRACKET and colorindex < len(colors) - 1: colorindex += 1
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if colorindex != 0: wps.append((mouseX, mouseY, colors[colorindex]))
            else: wps.append((mouseX, mouseY))#; print('mouse was clicked!')


        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d): changedX = 0#; ismoving = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s): changedY = 0#; ismoving = False


    mouseX, mouseY = pygame.mouse.get_pos()

    if mouseIsPressed: wps.append((mouseX, mouseY)); print('mouse was clicked!'); mouseIsPressed = False

    # player movement
    if ismoving:
        plX += changedX
        plY += changedY

    # restricting the player inside the window
    if plX <= 0:
        plX = 0
    elif plX >= windratio[0]:
        plX = windratio[0]
    
    if plY <= 0:
        plY = 0
    elif plY >= windratio[1]:
        plY = windratio[1]
    
    #if isReset:
        #plx = windratio[0] // 2; ply = windratio[1] // 2
        #isReset = False

    if pixelmode: drawpixelgrid()
    showWpoints(0, 0)
    if SHOWACTUALCOORDS: showtruecoords(0, 35)
    else: showcoords(0, 35)
    showcolor(0, 70)
    #showcursorpos(0, 70)
    #print(f'Y:{plY}')

    placeWaypoints()
    drawWPlines()
    player(plX, plY, plicon)

    clock.tick(60)

    pygame.display.update()