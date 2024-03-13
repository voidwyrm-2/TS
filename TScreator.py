import pygame








def limit(input, max):
    if input > max: return max
    return input

def limitmin(input, min):
    if input < min: return min
    return input



def log(data):
    with open('LOG.txt', 'at') as flog: flog.write(str(data) + '\n')

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

mouseDrawMode = False

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
def player(px, py):
    global pixelmode
    playerradius = 7
    if pixelmode: playerradius = 5
    pygame.draw.circle(screen, (0, 0, 255), (px, py), playerradius)


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
    colorval = colorvals[list(colorvals.keys())[colorindex]]
    if pixelmode and list(colorvals.keys())[colorindex] == 'black': colorval = (100, 100, 100)
    dacolor = mainfont.render(f'{list(colorvals.keys())[colorindex]}', True, colorval); screen.blit(dacolor, (x, y + 35))


def showMDM(x, y):
    mdmode = 'MD Mode: off'
    if mouseDrawMode: mdmode = 'MD Mode: on'
    mdm = mainfont.render(mdmode, True, (255, 255, 255))
    screen.blit(mdm, (x, y))


def showtruecoords(x, y):
    truco = mainfont.render(f'plX:{plX},plY:{plY}', True, (255, 255, 255))
    #co = mainfont.render(f'plX:{plX},plY:{plY}', True, (255, 255, 255))
    screen.blit(truco, (x, y))


def placeWaypoints():
    wpsize = 5
    if pixelmode: wpsize = 2
    for w in wps:
        if len(w) >= 3:
            linecolorB = colorvals[w[2]]
            if pixelmode and w[2] == 'black': linecolorB = (100, 100, 100)
            pygame.draw.circle(screen, linecolorB, (w[0], w[1]), wpsize)
        else:
            pointcolorA = (50, 50, 50)
            if pixelmode: pointcolorA = (100, 100, 100)
            pygame.draw.circle(screen, pointcolorA, (w[0], w[1]), wpsize)

def drawWPlines():
    for p in range(len(wps)):
        p1 = wps[limit(p, len(wps) - 1)]
        p2 = wps[limit(p + 1, len(wps) - 1)]
        if len(p2) >= 3:
            linecolorD = colorvals[p2[2]]
            if pixelmode and p2[2] == 'black': linecolorD = (100, 100, 100)
            pygame.draw.line(screen, linecolorD, (p1[0], p1[1]), (p2[0], p2[1]), 3)
        else:
            linecolorC = (50, 50, 50)
            if pixelmode: linecolorC = (100, 100, 100)
            pygame.draw.line(screen, linecolorC, (p1[0], p1[1]), (p2[0], p2[1]), 3)


def drawsquare(X, Y, radius):
    global wps
    wps.append((X + radius, Y + radius))
    wps.append((X - radius, Y + radius))
    wps.append((X - radius, Y - radius))
    wps.append((X + radius, Y - radius))
    wps.append((X + radius, Y + radius))


def drawcircle(X, Y, radius, points):
    global wps
    wps.append((X + radius, X + radius))
    wps.append((X + radius, Y + (radius // 2)))
    wps.append((X - radius, Y + radius))
    wps.append((X - radius, Y - radius))
    wps.append((X + radius, Y - radius))
    wps.append((X + radius, Y + radius))
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


def conformplayer():
    global changedX
    global changedY
    global plX
    global plY
    for pixX in range(0, windratio[0], 10):
        changedX = 0
        #print(f'checking {pixX} on X axis...')
        pOrigX = plX
        pDistX = plX - pixX
        if pDistX < 10 and pDistX > -1: plX = pixX; print(f'found close coord({pixX}) to player\'s({pOrigX}) on X axis!'); break
    for pixY in range(0, windratio[1], 10):
        changedY = 0
        #print(f'checking {pixY} on Y axis...')
        pOrigY = plY
        pDistY = plY - pixY
        if pDistY < 10 and pDistY > -1: plY = pixY; print(f'found close coord({pixY}) to player\'s({pOrigY}) on Y axis!'); break

def conformwaypoint(waypX: int, waypY: int):
    global wps

    outX = 0
    outY = 0

    for pixX in range(0, windratio[0], 10):
        pOrigX = waypX
        pDistX = waypX - pixX
        if pDistX < 10 and pDistX > -1: outX = pixX; print(f'found close coord({pixX}) to waypoint\'s({pOrigX}) on X axis!'); break
    for pixY in range(0, windratio[1], 10):
        pOrigY = waypY
        pDistY = waypY - pixY
        if pDistY < 10 and pDistY > -1: outY = pixY; print(f'found close coord({pixY}) to waypoint\'s({pOrigY}) on Y axis!'); break
    
    #print(f'{outX}, {outY}')
    return (outX, outY)



def instructs(wayp: list):
    out = ''
    if len(wayp) <= 0: return
    for co in wayp:
        if len(co) >= 3: ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))},{co[2]}'
        else: ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))}'
        out = out + f'{ins}/'
    #if out[-1] == '/': del out[-1]
    return f'{convertx(wayp[0][0], windratio[0])},{fixY(converty(wayp[0][1], windratio[1]))},white/{out.removesuffix("/")}'


def save(turstructs: str):
    if savetofile:
        savename = input('please type a name\n')
        with open(f'drawings/{savename}.txt', 'xt') as savefile: savefile.write(turstructs)
        print('TS instructions generated')
    else: print(turstructs)


def backup():
    with open('BACKUP.txt', 'wt') as bkup: bkup.write(instructs(wps))



running = True
while running:
    screen.fill((0, 0, 0))  # background
    
    #backup()

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

            if event.key == pygame.K_1: drawsquare(plX, plY, 20)#; print(wps)

            if event.key == pygame.K_2: drawcircle(plX, plY, 20, 20); print(wps)

            if event.key == pygame.K_0:
                if pixelmode: wps.append(((windratio[0] // 2) + 4,(windratio[1] // 2) + 4))
                else: wps.append((windratio[0] // 2,windratio[1] // 2))
            
            if event.key == pygame.K_LEFTBRACKET and colorindex > 0: colorindex -= 1
            if event.key == pygame.K_RIGHTBRACKET and colorindex < len(colors) - 1: colorindex += 1
            
            if event.key == pygame.K_COMMA and not pixelmode: conformplayer(); pixelmode = True#; print(f'pixelmode is now on({pixelmode})')
            if event.key == pygame.K_PERIOD and pixelmode: pixelmode = False#; print(f'pixelmode is now off({pixelmode})')

            if event.key == pygame.K_n and not mouseDrawMode: mouseDrawMode = True
            if event.key == pygame.K_m and mouseDrawMode: mouseDrawMode = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouseDrawMode:
                if pixelmode:
                    conformed = conformwaypoint(mouseX, mouseY)
                    if colorindex != 0: wps.append((conformed[0], conformed[1], colors[colorindex]))
                    else: wps.append((conformed[0], conformed[1]))
                else:
                    if colorindex != 0: wps.append((mouseX, mouseY, colors[colorindex]))
                    else: wps.append((mouseX, mouseY))
            else:
                mouseIsPressed = True
            
            #print('mouse was clicked!')

        if event.type == pygame.MOUSEBUTTONUP: mouseIsPressed = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d): changedX = 0#; ismoving = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s): changedY = 0#; ismoving = False


    mouseX, mouseY = pygame.mouse.get_pos()

    if mouseIsPressed and mouseDrawMode:
        if pixelmode:
            conformed = conformwaypoint(mouseX, mouseY)
            if colorindex != 0: wps.append((conformed[0], conformed[1], colors[colorindex]))
            else: wps.append((conformed[0], conformed[1]))
        else:
            if colorindex != 0: wps.append((mouseX, mouseY, colors[colorindex]))
            else: wps.append((mouseX, mouseY))
        
        #print('mouse was clicked!'); mouseIsPressed = False

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
    showMDM(0, 140)
    #showcursorpos(0, 70)
    #print(f'Y:{plY}')

    placeWaypoints()
    drawWPlines()
    player(plX, plY)

    clock.tick(60)

    pygame.display.update()
