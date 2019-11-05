"""一个多面🎲模块尝试"""

from random import randint


class Die():        # 🎲英文dice/die皆可
    '''自定义多面骰子🎲'''
    def __init__(self,sides=6):     
        '''面数属性，默认六面体'''
        self.sides = sides        
    def roll_die(self):            
        '''摇动骰子'''
        x1 = randint(1,self.sides)
        print(str(x1)+"点")
        
die_6 = Die()   # 括号内可定义几面体，默认6
die_10 = Die(10)
die_20 = Die(20)

for x in range(10):     # 投掷10次
    die_6.roll_die()    # 投掷一次
print("以上是"+str(die_6.sides)+"面体，投掷 "+str(x+1)+"次结果.\n")

for x in range(10):     # 投掷10次
    die_10.roll_die()    # 投掷一次试验
print("以上是"+str(die_10.sides)+"面体，投掷 "+str(x+1)+"次结果.\n")

for x in range(10):     # 投掷10次
    die_20.roll_die()    # 投掷一次试验
print("以上是"+str(die_20.sides)+"面体，投掷 "+str(x+1)+"次结果.\n")


