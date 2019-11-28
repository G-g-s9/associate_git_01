import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''初始化外星人相应属性并确定其起始位置'''
    def __init__(self,ai_settings,screen):  #ai_settings过渡传参，本类中无调用，但要写进属性中(后来加了个外星人高设置，这里就用上了)
        super().__init__()     #继承Sprite的属性方法
        self.screen = screen    #传参屏幕属性
        self.ai_settings = ai_settings  #传参设置属性

        #外星人图片载入及其初始位置确立
        # ~ self.image = pygame.image.load("images/alien.png")  #加载外星人图
        self.image = pygame.image.load("images/monster.png")  #加载团子图（置换上一条使用）

        #锁定比例变换尺寸
        self.rect = self.image.get_rect()    #获得外星人图片rect属性
        self.scale = float(self.rect.width)/float(self.rect.height)     #记录原图比例
        self.size = int(ai_settings.alien_h*self.scale),ai_settings.alien_h       #调整为高49px，宽随比例给出
        self.image = pygame.transform.scale(self.image,self.size)
        # ~ self.image.set_alpha(2)         #失败了这个，后面再优化了。。。本来想让外星人透明点
        self.rect = self.image.get_rect()    #获得实际显示外星人图片rect属性

        self.rect.x = self.rect.width       #这里x坐标，在外星人群建立后失效】初始x坐标，屏幕左上角隔着一个外星人的宽
        self.rect.y = self.rect.height      #初始y坐标，屏幕左上角隔着一个外星人的高

        self.x = float(self.rect.x)     #x坐标浮点化，可相对微调

    def blitme(self):
        '''指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)     #将图片绘制到屏幕指定的坐标（上面那个rect的左上角坐标位置）


