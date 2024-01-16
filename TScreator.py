import pygame



# initialize game
pygame.init()

# creating a screen
screen = pygame.display.set_mode((600, 600))  # passing width and height
screen.fill("black")
pygame.display.flip()
# title and icon
pygame.display.set_caption("TSCreator")
#icon = pygame.image.load('')
#pygame.display.set_icon(icon)
#pygame.draw.rect()

pygame.font.init()
mainfont = pygame.font.Font('freesansbold.ttf', 32)


wps = []
plicon = pygame.image.load('Turt.png')
plgif = [pygame.image.load('Turt_f1.png'), pygame.image.load('Turt_f2.png')]
plX = 0
plY = 0
speed = 5
changedX = 0
changedY = 0
isWalking = False
wRight = False
wLeft = False
def player(px, py, icon): screen.blit(icon, (px, py))



def showWpoints(x, y):
    wp = mainfont.render(f'Waypoints: {len(wps)}', True, (255, 255, 255))
    screen.blit(wp, (x, y))

def showcoords(x, y):
    co = mainfont.render(f'plX:{plX},plY:{plY}', True, (255, 255, 255))
    screen.blit(co, (x, y))


def placeWaypoints():
    for w in wps:
        pygame.draw.circle(screen, (255, 0, 0), w, 5)


def convert(wayp: list):
    out = ''
    if len(wayp) <= 0: return
    for co in wayp:
        ins = f'{co[0]},{co[1]}'
        out = out + f'{ins}/'
    #if out[-1] == '/': del out[-1]
    return out






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

                if event.key == pygame.K_LEFT or event.key == pygame.K_a: changedX = -speed

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: changedX = speed

                if event.key == pygame.K_UP or event.key == pygame.K_w: changedY = -speed

                if event.key == pygame.K_DOWN or event.key == pygame.K_s: changedY = speed

                if event.key == pygame.K_o:
                    if len(wps) >= 1: del wps[-1]

                if event.key == pygame.K_p: print(convert(wps))


        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d): changedX = 0
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s): changedY = 0


    # player movement
    plX += changedX
    plY += changedY

    # restricting the player inside the window
    if plX <= -10:
        plX = -10
    elif plX >= 550:
        plX = 550
    
    if plY <= -10:
        plY = -10
    elif plY >= 550:
        plY = 550
    
    placeWaypoints()
    showWpoints(100, 20)
    showcoords(300, 50)

    player(plX, plY, pygame.image.load('Turt.png'))
    pygame.display.update()
