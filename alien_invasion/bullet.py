import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):       #继承导入的Sprite类
    '''飞船子弹管理类'''

    def __init__(self,ai_settings,screen,ship):  #主要追加
        '''飞船对象位置创建一个子弹对象'''
        super(Bullet,self).__init__()       #调用Sprite父类方法。__init__（）,使Bullet包含父类属性.另,surper形参python3.+可以省略不写
        self.screen = screen        #追加属性

        #在（0,0）处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx      #与飞船水平对齐
        self.rect.top = ship.rect.top+ai_settings.bullet_height/10   #与飞船垂直对齐,出头1/10的子弹高度

        #存储用小数位置表示的子弹位置(不考虑惯性,简化为直线飞行,光y坐标变化）
        self.y = float(self.rect.y)     #这里是Rect的y坐标,也可以下面这种
        # ~ self.y = float(self.rect.centery)

        #颜色速度设置传参
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动位置,无条件的一直向上，向上。。。'''
        self.y -= self.speed_factor     #这里是浮点数
        self.rect.y = self.y    #正式传回子弹块位置,实际就截取了整数

    def draw_bullet(self):
        '''绘制子弹,就是显示,注意图层顺序'''
        pygame.draw.rect(self.screen,self.color,self.rect)  #在screen上指定rect位置,填充color。非加载图片的,要draw矩形块
