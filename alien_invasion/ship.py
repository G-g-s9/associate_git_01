'''假装是飞船模块,实际是用Sword代替图'''

import pygame

class Ship():
    
    def __init__(self,screen):
        '''初始化飞船便设置其初始位置'''
        self.screen = screen
        
        # 加载飞船图像并获取其外接矩形
        ship_pic_source = 'images/ship.png' # 飞船图形来源
        self.image = pygame.image.load(ship_pic_source).convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80)) # 素材图太大，调整为80px*80px
        self.rect = self.image.get_rect()
        self.screen_rect =screen.get_rect()
        
        # 将每艘飞船放在屏幕底部居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
