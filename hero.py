from WarGlobalVar import *
from threading import Thread
import copy
class controlHERO(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        while True:
            Hero_Status[self.name].getPlayerMovement()
            #FPSCLOCK.tick(FPS)
class HERO():
    blood = 100
    direction = RIGHT
    attackValue = 3
    def __init__(self, name='Knight', color=WHITE):
        self.name = name
        self.color = color
        nextPoint = self.getRandomLocation()
        #if nextPoint is forbidden, keep coord unchanged
        while (self.checkOverRule(nextPoint) == False or\
                self.checkEdgeRule(nextPoint) == False):
            nextPoint = self.getRandomLocation()
        self.coord = nextPoint
        return

    def getRandomLocation(self):
        return {'x': random.randint(0,CELLWIDTH -1), 'y': random.randint(0,CELLHEIGHT -1)}

    def getPlayerMovement(self):
        nextPoint = self.coord.copy()
        # 获取键盘事件（上下左右按键）
        key_pressed = pygame.key.get_pressed()

        # 处理键盘事件（移动飞机的位置）
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.direction = UP
            nextPoint['y'] = nextPoint['y'] - 1
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.direction = DOWN
            nextPoint['y'] = nextPoint['y'] + 1
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.direction = LEFT
            nextPoint['x'] = nextPoint['x'] - 1
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.direction = RIGHT
            nextPoint['x'] = nextPoint['x'] + 1
        '''
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.direction = LEFT
                    nextPoint['x'] = nexPoint['x'] - 1
                elif event.key == K_RIGHT:
                    self.direction = RIGHT
                    nextPoint['x'] = nextPoint['x'] + 1
                elif event.key == K_UP:
                    self.direction = UP
                    nextPoint['y'] = nextPoint['y'] - 1
                #elif evnt.key == K_DOWN:
                else:
                    self.direction = K_DOWN
                    nextPoint['y'] = nextPoint['y'] + 1
        '''
        if (self.checkEdgeRule(nextPoint) == True and self.checkOverRule(nextPoint) == True):
            #print('nextPoint',nextPoint)
            self.coord = {'x': nextPoint['x'], 'y': nextPoint['y']}
        else:
            print('can not go to nextPoint')

        return nextPoint

    def checkEdgeRule(self,checkcoord):
        if (checkcoord['x'] > (CELLWIDTH-1) or\
                checkcoord['x'] < 0 or\
                checkcoord['y'] > (CELLHEIGHT - 1) or\
                checkcoord['y'] < 0):
            return False
        else:
            return True

    def dead(self,hero):
        hero.coord = {'x':-10, 'y':-10}

    # avoid different rectangle at the same location
    def checkOverRule(self,coord):
        for key in ArmyA_Status:
            if (ArmyA_Status[key].coord['x'] == coord['x'] and\
                    ArmyA_Status[key].coord['y'] == coord['y'] and\
                    key != self.name):
                return False
        for key in ArmyB_Status:
            if (ArmyB_Status[key].coord['x'] == coord['x'] and\
                    ArmyB_Status[key].coord['y'] == coord['y'] and\
                    key != self.name):
                return False
        return True

    def chooseEnemy(self, direction):
        if self.color == Army_B_Color:
            pass

    def attack(self):
        Enemy = self.chooseEnemy(self.direction)
        if Enemy == None:
            print("Enemy None")
            #没有找到敌人就等待玩家动作
            self.getPlayerMovement()
        else:
            print("find Enemy")
            if self.isInAttackArea(Enemy):
                print("in attackArea")
                Enemy.blood = Enemy.blood - self.attackValue
            if Enemy.blood <= 0:
                self.dead(Enemy)

    def isInAttackArea(self,Enemy):
        if (abs(Enemy.coord['x'] - self.coord['x'])\
                + abs(Enemy.coord['y'] - self.coord['y'])\
                == 1):
            return True
        else:
            return False

    def terminate(self):
        passs
