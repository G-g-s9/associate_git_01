'''假装是飞船模块,实际是用Sword代替图'''

import pygame       # 导入pygame模块

class Ship():
    # ~ '''飞船的图像、大小、位置、移动速度等属性'''
    def __init__(self,ai_settings,screen):
        '''初始化飞船便设置其初始位置'''
        self.screen = screen    # 传递屏幕参数
        self.ai_settings = ai_settings  # 传递设置里的飞船速度参数

        # 加载飞船图像并获取其外接矩形
        ship_pic_source = 'images/ship.png' # 飞船图形来源

        # 飞船素材载入即调整
        self.image = pygame.image.load(ship_pic_source).convert_alpha()     # 加载图像
        self.image = pygame.transform.scale(self.image,(49,49)) # 找来素材图太大，调整为49px*49px
        self.image = pygame.transform.rotate(self.image,180)    # 旋转，剑尖朝上

        self.rect = self.image.get_rect()   # 获得 素材图rect对象属性(传递宽高
        self.screen_rect =screen.get_rect() # 获得 屏幕rect对象属性(传递宽高

        # 将每艘飞船放在屏幕底部居中
        self.rect.centerx = self.screen_rect.centerx    # 屏幕的水平中心值 赋给 素材图水平中值。即以 屏幕为参考系，素材图水平居中对齐
        self.rect.bottom = self.screen_rect.bottom      # 屏幕为参考系，素材图底对齐（y值）

        # 在飞船的属性center中存储小数值
        self.center =float(self.rect.centerx)

        # 移动标记，默认假，即不动
        self.moving_right = False   # 右移假
        self.moving_left = False   # 左移假

    def update(self):   # 刷新飞船位置
        '''移动标记为真就调整飞船位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:       # 右移标记为真 且 飞船右边没碰到窗口右边
            self.center +=self.ai_settings.ship_speed_factor   # 飞船矩形块水平位置属性值加X，即右移
        if self.moving_left and self.rect.left > 0:       # ~ 左移标记为真 且 飞船左边没碰到窗口左边（centerx=0）   注意这里不用 elif(以防右移一直优先判断。比如同时按下，则右移，而非抵消不动
            self.center -=self.ai_settings.ship_speed_factor   # 飞船矩形块水平位置属性值减X，即左移

        # 根据self.center(速度因素接受浮点数)更新飞船rect值
        self.rect.centerx = self.center     #  self.rect.centerx 将只存储 self.center 的整数部分，但对显示飞船而言，这问题不大

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)      # 块传输。根据素材图rect属性（centerx，bottom）
