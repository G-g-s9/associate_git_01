'''假装是飞船模块,实际是用Sword代替图'''

import pygame       # 导入pygame模块

class Ship():
    # ~ '''飞船的图像、大小位置等'''
    def __init__(self,screen):
        '''初始化飞船便设置其初始位置'''
        self.screen = screen    # 获得屏幕参数

        # 加载飞船图像并获取其外接矩形
        # ~ ship_pic_source = 'images/ship.png' # 飞船图形来源
        ship_pic_source = r'/home/e/桌面/projects_new_start/alien_invasion/images/ship.png' # 非当前目录下，改，飞船图形来源
        self.image = pygame.image.load(ship_pic_source).convert_alpha()     # 加载图像
        self.image = pygame.transform.scale(self.image,(80,80)) # 素材图太大，调整为80px*80px
        self.rect = self.image.get_rect()   # 获得 素材图rect属性，宽高
        self.screen_rect =screen.get_rect() # 获得 屏幕rect属性，宽高

        # 将每艘飞船放在屏幕底部居中
        self.rect.centerx = self.screen_rect.centerx    # 屏幕的水平中心值 赋给 素材图水平中值。即以 屏幕为参考系，素材图水平居中对齐
        self.rect.bottom = self.screen_rect.bottom      # 屏幕为参考系，素材图底对齐（y值）

        # 移动标记，默认假，即不动
        self.moving_right = False   # 右移假
        self.moving_left = False   # 左移假

    def update(self):   # 刷新飞船位置
        '''移动标记为真就调整飞船位置'''
        if self.moving_right:       # 右移标记为真
            self.rect.centerx +=1   # 飞船矩形块水平位置属性值加一，即右移
        if self.moving_left:       # ~ 左移标记为真   注意这里不用 elif(以防右移一直优先判断。比如同时按下，则右移，而非抵消不动
            self.rect.centerx -=1   # 飞船矩形块水平位置属性值减一，即左移

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)      # 块传输。根据素材图rect属性（centerx，bottom）
