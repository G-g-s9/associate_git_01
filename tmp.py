'''tmp 随用随删'''


a,b,c,d = 'wo ',9,4,4+9j
print(type(d))

# ~ filename = "pi_digits.txt"              # 测试附加内容。每次运行都会添加一次
# ~ with open(filename,'a') as file_object:
    # ~ file_object.write("hahhahah")


c = "jkjkjkJ"
print(c.count("j"))
print(c.lower().count("j"))
# ~ print(c.count("j").lower())         # 错误代码，属性是从左到右的


import json

numbers = [3,4,6,5,8]

filename = "numbers.json"
with open(filename,"w") as f:       # 新建一个json文件，把数组方进去
    view1 = json.dump(numbers,f)            # 转储数据

with open(filename) as t:
    view2 = json.load(t)

print(view1)
# ~ print(view2)

dict = {'Name': 'Runoob', 'Age': 27}
print ("Age 值为 : ",dict.get('Age'))


print(str({'google': 'google.com', 'runoob': 'runoob.com'}),"\n\n\n\n")


#####################################
a = a_x,a_y = 600,800
print(a)
print(a_y)

print(int(2.49))    #截取整数





import pygame
import sys
from pygame.locals import *
from random import *
# pygame.sprite.Sprite 代表游戏对象的简单基类
class Ball(pygame.sprite.Sprite):
    def __init__(self,image,position,speed,bg_size):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__() # 注意 super 的格式
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0],bg_size[1]
        # 由于采用 collide_circle()方法检测圆的碰撞，所以需要设置 radius 属性
        self.radius = self.rect.width / 2
    def move(self):
        '''移动圆形的rect'''
        self.rect = self.rect.move(self.speed)
        # 这里要的效果是小球整个超出屏幕左侧的应对方案
        if self.rect.right < 0:
            self.rect.left = self.width
        elif self.rect.left > self.width:
            self.rect.right = 0
        elif self.rect.bottom <0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0
def main():
    pygame.init()
    ball_image = "gray_ball.png"
    bg_image = "background.png"

    running = True
    #根据背景图片设置游戏界面的尺寸
    bg_size = width,height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball")
    background = pygame.image.load(bg_image).convert_alpha()
    # 用来存放小球对象的列表
    balls = []
    group = pygame.sprite.Group()

    # 创建五个小球，位置随机，速度随机
    for i in range(5):      #数量接近满屏时，容易死循环
        # 球的大小是 100 x 100 防止越出边界，所以要宽和高减 100 的范围以内
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(-10,10),randint(-10,10)]
        ball = Ball(ball_image,position,speed,bg_size)
        # 创建小球时需要检测，防止球与球之间发生重叠
        # while pygame.sprite.spritecollide(ball,group,False):
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
            # 创建小球时，若发生碰撞即有重叠，就重新分配位置
            ball.rect.left,ball.rect.top = randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        # 新建一个球后，将其加入检测组中
        group.add(ball)

    clock = pygame.time.Clock() # 设置帧率

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background,(0,0))

        for each in balls:
            each.move()
            screen.blit(each.image,each.rect)

        for each in group:
            # 检测组中每一个小球运动过程中是否发生碰撞
            # 先将其弹出，检测完后再加入
            group.remove(each)
            # 若发生碰撞，就运动方向改为相反方向
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            group.add(each)
        pygame.display.flip()
        clock.tick(30) #最高每秒不超过 30 次

if __name__ == '__main__':
    main()
