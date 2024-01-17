import pygame








def limit(input, max):
    if input > max: return max
    return input




def log(data):
    with open('LOG.txt', 'at') as flog: flog.write(str(data) + '\n')


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

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)

savetofile = True
pixelmode = True

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


def reversex(num: int, max: int):
    nums = []
    for n in range(max - 1):
        if n != 0: nums.append(n)
    return -nums[num - 1]

def reversey(num: int, max: int):
    nums = []
    for n in range(max - 1):
        if n != 0: nums.append(n)
    #log(f'Y:{nums}')
    return -nums[num - 1]


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


def placeWaypoints():
    wpsize = 5
    if pixelmode: wpsize = 2
    for w in wps:
        pygame.draw.circle(screen, (255, 0, 0), w, wpsize)

def drawWPlines():
    for p in range(len(wps)):
        pygame.draw.line(screen, (250, 0, 0), wps[limit(p, len(wps) - 1)], wps[limit(p + 1, len(wps) - 1)])


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
        ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))}'
        out = out + f'{ins}/'
    #if out[-1] == '/': del out[-1]
    return out


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

                if event.key == pygame.K_RETURN: wps.append((plX, plY))

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

                #if event.key == pygame.K_x: changedX = 0; plx = windratio[0] // 2

                #if event.key == pygame.K_y: changedY = 0; ply = windratio[1] // 2

                if event.key == pygame.K_z: wps.append(0,0) #changedX = 0; changedY = 0; isReset = True

                #if event.key == pygame.K_r: plx = 0; ply = 0; wps.clear()

                if event.key == pygame.K_p: save(instructs(wps))


        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d): changedX = 0#; ismoving = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s): changedY = 0#; ismoving = False


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

    placeWaypoints()
    drawWPlines()
    showWpoints(0, 0)
    showcoords(0, 35)
    #print(f'Y:{plY}')

    player(plX, plY, plicon)
    pygame.display.update()