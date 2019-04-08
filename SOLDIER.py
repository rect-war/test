from WarGlobalVar import *
from hero import *

class SOLDIER:
    blood = 10
    attackValue = 2
    attackArea = 15
    def checkEdgeRule(self,checkcoord):
        if (checkcoord['x'] > (CELLWIDTH - 1) or\
                checkcoord['x'] < 0 or\
                checkcoord['y'] > (CELLHEIGHT - 1) or\
                checkcoord['y'] < 0):
            return False
        else:
            return True



    def __init__(self, name, color):
        self.name = name
        self.color = color
        nextPoint = self.getRandomLocation()
        while (self.checkOverRule(nextPoint) == False or
                self.checkEdgeRule(nextPoint) == False):
            nextPoint = self.getRandomLocation()
        self.coord = nextPoint
        return

    def dead(self,soldier):
        soldier.coord = {'x':-10,'y':-10}

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
        '''
        for key in Hero_Status:
            if (Hero_Status[key].coord['x'] == coord['x'] and\
                    Hero_Status[key].coord['y'] == coord['y'] and\
                    key != self.name):
                return False
        '''

        if (Hero_Status['Knight'].coord['x'] == coord['x'] and\
                Hero_Status['Knight'].coord['y'] == coord['y'] and\
                Hero_Status['Knight'].name != self.name):
            return False

        # ensure have already checking everybody Location

        return True

    def getRandomLocation(self):
        return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}

    def searchEnemy(self,step):
        if self.color != Hero_Status['Knight'].color:
            for i in range(1,step):
                for key in Hero_Status:
                    if abs(Hero_Status[key].coord['x'] - self.coord['x'])\
                       + abs(Hero_Status[key].coord['y'] - self.coord['y'])\
                       == i and Hero_Status[key].blood > 0:
                        return Hero_Status[key]


        if self.color == Army_B_Color:
            for i in range(1,step):
                for key in ArmyA_Status:
                    if abs(ArmyA_Status[key].coord['x'] - self.coord['x'])\
                       + abs(ArmyA_Status[key].coord['y'] - self.coord['y'])\
                       == i and ArmyA_Status[key].blood > 0:
                        return ArmyA_Status[key]

        if self.color == Army_A_Color:
            for i in range(1,step):
                for key in ArmyB_Status:
                    if abs(ArmyB_Status[key].coord['x'] - self.coord['x'])\
                       + abs(ArmyB_Status[key].coord['y'] - self.coord['y'])\
                       == i and ArmyB_Status[key].blood > 0:
                        return ArmyB_Status[key]
        return None

    def attack(self):
        #search Enemy in the nearest 10 grids.
        Enemy = self.searchEnemy(self.attackArea)
        if Enemy == None:
            #print('Enemy None')
            self.moveCasually()
        else:
            #print('find Enemy')
            if self.isInAttackArea(Enemy):
                #print("in attackArea")
                Enemy.blood = Enemy.blood - self.attackValue
            else:
                #print("moveto Enemy")
                self.moveto(Enemy)
                if self.isInAttackArea(Enemy):
                    Enemy.blood = Enemy.blood - self.attackValue
            if Enemy.blood <= 0:
                self.dead(Enemy)

    def moveto(self,Enemy):
        deltax = abs(Enemy.coord['x'] - self.coord['x'])
        deltay = abs(Enemy.coord['y'] - self.coord['y'])
        nextPoint = {'x':self.coord['x'], 'y':self.coord['y']}
        if deltay > deltax and Enemy.coord['y'] < self.coord['y']:
            nextPoint['y'] = nextPoint['y'] - 1
        elif deltay > deltax and Enemy.coord['y'] >= self.coord['y']:
            nextPoint['y'] = nextPoint['y'] + 1
        elif deltay <= deltax and Enemy.coord['x'] < self.coord['x']:
            nextPoint['x'] = nextPoint['x'] - 1
        elif deltay <= deltax and Enemy.coord['x'] >= self.coord['x']:
            nextPoint['x'] = nextPoint['x'] + 1
        else:
            #print('moveto error')
            pass
        if (self.checkEdgeRule(nextPoint) == True and self.checkOverRule(nextPoint) == True):
            self.coord = {'x': nextPoint['x'], 'y': nextPoint['y']}
            #print('nextPoint')
            #print(nextPoint)
        else:
            pass
            #print('can not go to nextPoint')

    def isInAttackArea(self,Enemy):
        if abs(Enemy.coord['x'] -self.coord['x'])\
           + abs(Enemy.coord['y'] - self.coord['y'])\
           == 1:
            return True
        else:
            return False


    def moveCasually(self):
        direct = random.randint(1, 4)
        Point = {'x': self.coord['x'], 'y': self.coord['y']}
        #print('ok')
        #print(self.coord)
        if direct == 1:
            #print(1)
            Point['x'] = Point['x']
            Point['y'] = Point['y'] - 1
        elif direct == 2:
            #print(2)
            Point['x'] = Point['x']
            Point['y'] = Point['y'] + 1
        elif direct == 3:
            #print(3)
            Point['x'] = Point['x'] - 1
            Point['y'] = Point['y']
        else:
            #print(4)
            Point['x'] = Point['x'] + 1
            Point['y'] = Point['y']
        if (self.checkEdgeRule(Point) == True and self.checkOverRule(Point) == True):
            self.coord = {'x': Point['x'], 'y': Point['y']}
            #print(self.coord)
        #print(self.coord)

    def escapefrom(self,Enemy):
        deltax = abs(Enemy.coord['x'] - self.coord['x'])
        deltay = abs(Enemy.coord['y'] - self.coord['y'])
        nextPoint = {'x':self.coord['x'], 'y':self.coord['y']}
        if deltay < deltax and Enemy.coord['y'] < self.coord['y']:
            nextPoint['y'] = nextPoint['y'] + 1
        elif deltay < deltax and Enemy.coord['y'] >= self.coord['y']:
            nextPoint['y'] = nextPoint['y'] - 1
        elif deltay >= deltax and Enemy.coord['x'] < self.coord['x']:
            nextPoint['x'] = nextPoint['x'] + 1
        elif deltay >= deltax and Enemy.coord['x'] >= self.coord['x']:
            nextPoint['x'] = nextPoint['x'] - 1
        else:
            pass
            #print('moveto error')
        if (self.checkEdgeRule(nextPoint) == True and self.checkOverRule(nextPoint) == True):
            self.coord = {'x': nextPoint['x'], 'y': nextPoint['y']}

        return


    def terminate(self):
        pygame.quit()
        sys.exit()
