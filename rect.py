from SOLDIER import *
from hero import *
Awin = 0
Bwin = 0
tie = 0
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    global ArmyA_Status, ArmyB_Status, Hero_Status
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('War')
    while True:
        initWarGame()
        runGame()


def initWarGame():
    global Hero_Status
    DISPLAYSURF.fill(BGCOLOR)
    drawGrid()
    drawPressMsg()
    Hero_Status['Knight'] = HERO('Knight', Army_A_Color)
    for i in range(Army_A_Num):
        ArmyA_Status['A'+ str(i)] = SOLDIER('A'+str(i), Army_A_Color)
    for i in range(Army_B_Num):
        ArmyB_Status['B'+ str(i)] = SOLDIER('B'+str(i), Army_B_Color) 
    #t = controlHERO('Knight')
    #t.start()

def runGame():
    global Hero_Status
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        checkForKeyPress()
        drawGrid()
        drawPressMsg()
        #print("start")

        for i in range(Army_A_Num):
            if ArmyA_Status['A'+ str(i)].blood > 0:
                ArmyA_Status['A'+ str(i)].attack()
        for i in range(Army_B_Num):
            if ArmyB_Status['B'+ str(i)].blood > 0:
                ArmyB_Status['B'+ str(i)].attack()
        Hero_Status['Knight'].getPlayerMovement()

        BlockFlush()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        result = checkGameOver()
        if not result is None:
            return result
'''
        #----Strategy-----------
        for key in ArmyA_Status:
            if ArmyA_Status[key].blood > 0:
                Enemy = ArmyA_Status[key].searchEnemy(3)
                if Enemy is None:
                    ArmyA_Status[key].moveCasually()
                else:
                    ArmyA_Status[key].escapefrom(Enemy)
            else:
                ArmyA_Status[key].dead(ArmyA_Status[key])
        for key in ArmyB_Status:
            if ArmyB_Status[key].blood > 0:
                ArmyB_Status[key].attack()
            else:
                ArmyB_Status[key].dead(ArmyB_Status[key])

        #-----------------------
'''

def checkGameOver():
    global Awin, Bwin, tie
    #print ('rate')
    #print (Awin)
    #print (Bwin)
    #print (tie)
    Arest = 0
    Brest = 0
    for key in ArmyA_Status:
        if ArmyA_Status[key].blood > 0:
            Arest += 1
    for key in ArmyB_Status:
        if ArmyB_Status[key].blood > 0:
            Brest += 1
    if Arest == 0 and Brest == 0:
        tie = tie + 1
        return 'tie'
    elif Arest == 0 and Brest > 0:
        Bwin = Bwin + 1
        return 'Bwin'
    elif Arest > 0 and Brest == 0:
        Awin = Awin + 1
        return 'Awin'
    else:
        return None

def BlockFlush():
    for key in ArmyA_Status:
        if ArmyA_Status[key].blood > 0:
            drawBlock( ArmyA_Status[key].coord, ArmyA_Status[key].color )
    for key in ArmyB_Status:
        if ArmyB_Status[key].blood > 0:
            drawBlock( ArmyB_Status[key].coord, ArmyB_Status[key].color )
    if Hero_Status['Knight'].blood > 0:
            drawDoubleColorBlock(Hero_Status['Knight'].coord,\
                                    Hero_Status['Knight'].color,\
                                    WHITE)
    return

def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
    return None

def drawBlock(coord,color):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    BlockRect = pygame.Rect( x, y, CELLSIZE, CELLSIZE )
    pygame.draw.rect( DISPLAYSURF, color, BlockRect )

def drawDoubleColorBlock(coord,FOREcolor, BGcolor=WHITE):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    BGBlockRect = pygame.Rect(x , y, CELLSIZE, CELLSIZE)
    delta = CELLSIZE / 4
    FOREBlockRect = pygame.Rect(x+delta, y+delta, CELLSIZE/2 , CELLSIZE/2)
    pygame.draw.rect( DISPLAYSURF, BGcolor, BGBlockRect)
    pygame.draw.rect( DISPLAYSURF, FOREcolor, FOREBlockRect)


def drawGrid():
    for x in range( 2, WINDOWWIDTH, CELLSIZE ):
        pygame.draw.line( DISPLAYSURF, DARKGRAY, (x,2), (x,WINDOWHEIGHT))
    for y in range( 2, WINDOWHEIGHT, CELLSIZE ):
        pygame.draw.line( DISPLAYSURF, DARKGRAY, (2,y), (WINDOWWIDTH,y))

def drawPressMsg():
    global Awin, Bwin, tie
    pressKeySurf = BASICFONT.render('Awin:'+str(Awin)+' Bwin:'+str(Bwin)+\
                                    ' tie:'+str(tie), True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 202, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit( pressKeySurf, pressKeyRect )


def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
