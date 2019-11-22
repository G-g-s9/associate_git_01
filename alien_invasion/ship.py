'''
飞船模块（实际素材图是 剑Sword
包含飞船素材图加载调整、屏幕起始位置、移动速度、移动位置更新等属性，
'''

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

        self.rect = self.image.get_rect()   # 获得 素材图rect对象属性(传递参数，这里就用到宽高
        self.screen_rect =screen.get_rect() # 获得 屏幕rect对象属性(传递宽高

        # 起始位置——将每艘飞船放在屏幕底部居中
        self.rect.centerx = self.screen_rect.centerx    # 屏幕的水平中心值 赋给 素材图水平中值。即以 屏幕为参考系，素材图水平居中对齐
        self.rect.bottom = self.screen_rect.bottom      # 屏幕为参考系，素材图底对齐（y值）

        # 在飞船的属性center中存储小数值,注意对应xy轴
        self.centerx =float(self.rect.centerx)
        self.centery =float(self.rect.centery)

        # 移动标记，默认假，即不动 —— 控制飞船移动及其范围
        self.moving_right = False   # 右移假
        self.moving_left = False   # 左移假
        self.moving_top = False   # 上移假
        self.moving_bottom = False   # 下移假

    def update(self):   # 刷新飞船位置,并限制在一定范围内
        '''移动标记为真——调整飞船位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:       # 右移标记为真 且 飞船右边没碰到窗口右边
            self.centerx +=self.ai_settings.ship_speed_factor   # 飞船矩形块水平位置属性值加X，即右移
        if self.moving_left and self.rect.left > 0:       # ~ 左移标记为真 且 飞船左边没碰到窗口左边（centerx=0）   注意这里不用 elif(以防右移一直优先判断。比如同时按下，则右移，而非抵消不动
            self.centerx -=self.ai_settings.ship_speed_factor   # 飞船矩形块水平位置属性值减X，即左移
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:       # 下移标记为真 且 飞船底边没碰到窗口底边
            self.centery +=self.ai_settings.ship_speed_factor   # 飞船矩形块水平位置属性值加X，即右移
        if self.moving_top and self.rect.top > 10:       # ~ 上移标记为真 且 飞船顶部没碰到窗口顶部10px（centery=10以下）
            self.centery -=self.ai_settings.ship_speed_factor

        # 根据self.center(速度因素接受浮点数)更新飞船rect值
        self.rect.centerx = self.centerx     #  self.rect.centerx 将只存储 self.centerx 的整数部分，但对显示飞船而言，这问题不大
        self.rect.centery = self.centery

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)      # 块传输。根据素材图rect属性（centerx，bottom）
