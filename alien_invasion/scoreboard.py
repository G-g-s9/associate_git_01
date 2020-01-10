import pygame.font      #这里显示文字要用到
from pygame.sprite import Group   #编组容器类模块

from ship import Ship   #引用了ship


class Scoreboard():
    '''记分板，显示得分信息的类'''

    def __init__(self,screen,ai_settings,stats):
        '''初始化值，各种得分相关值'''
        self.screen = screen    #传参获得屏幕属性
        self.screen_rect = screen.get_rect()    #获得屏幕对应的矩形 用于对齐屏幕
        self.ai_settings = ai_settings      #传参获得设置的属性  一些传参
        self.stats = stats      #传参获得游戏实时统计值

        #显示得分信息的字体设置
        self.text_color = (255,0,0)         #字色，红
        self.font = pygame.font.Font('font/pingfang.ttf',36)    #字体苹方36

        #准备得分、最高得分、等级、剩余命 图像
        self.prep_score()   #调用👇下面2个渲染font
        self.prep_high_score()   #显示命历史最高得分函数准备
        self.prep_level()   #显示玩家等级函数准备
        self.prep_ships()   #显示命数函数准备
        
    def prep_ships(self):
        '''显示剩余命（显示飞船）'''
        self.ships = Group() #编组容器
        for ship_number in range(self.stats.ships_left):    #循环命数
            ship = Ship(self.ai_settings,self.screen)   #建个飞船实例
            ship.image = pygame.transform.scale(ship.image,(24,24)) #太大了，缩小到24
            ship.rect.x = 10 + ship_number * 24     #命数飞船x坐标
            ship.rect.y = 10     #命数飞船y坐标
            self.ships.add(ship)    #将建好小飞船实例加入ships组

    def prep_score(self):
        '''记分牌——得分信息渲染'''
        # ~ score_str = str(self.stats.score)    #转字符串
        round_score = round(self.stats.score,-1)    #保留有效数值-1位
        score_str = "{:,}".format(round_score)    #转字符串之数字格式化 {:,}表示以逗号为分隔符的数字形式
        self.score_image = self.font.render(score_str,True,self.text_color
                                            )  #创建一个指定surfer并在其上绘制文字，去掉最后背景色的参数self.ai_settings.bg_color也可，默认透明

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()     #获得渲染为图片的文字对应的矩形
        self.score_rect.right = self.screen_rect.right - 20 #位置屏幕左边空20
        self.score_rect.top =20 #位置屏幕顶部空20
        
    def prep_level(self):
        '''记玩家等级信息渲染 基本重用prep_score'''
        self.level_image = self.font.render('level:'+str(self.stats.level),True,
                                            self.text_color)  #去掉最后背景色的参数，默认透明

        #将得分放在屏幕右上角
        self.level_rect = self.level_image.get_rect()     #获得渲染为图片的文字对应的矩形
        self.level_rect.right = self.screen_rect.right - 20 #位置屏幕左边空20
        self.level_rect.top =20 + 36 #位置屏幕顶部空20+36
        
    def prep_high_score(self):
        '''将最高得分转换为渲染的图像'''
        high_socre = round(self.stats.high_score,-1)    #保留有效数值-1位
        high_score_str = "{:,}".format(high_socre)    #转字符串之数字格式化 {:,}表示以逗号为分隔符的数字形式
        high_score_str = '目前最高分'+high_score_str #加个文字提示
        self.high_score_image = self.font.render(high_score_str,True,
                                                self.text_color)    #转换为surfer
        #将历史最高分置于屏幕顶部居中
        self.high_score_rect = self.high_score_image.get_rect() #获取对应矩形区域
        self.high_score_rect.centerx = self.screen_rect.centerx #中心x坐标对应屏幕中心x坐标
        self.high_score_rect.top = self.screen_rect.top #顶部坐标对应屏幕顶部坐标
        
    def show_score(self):
        '''在屏幕上显示渲染好的文字图'''
        self.screen.blit(self.score_image,self.score_rect)  #将得分文字图绘制在其对应的rect位置上
        self.screen.blit(self.high_score_image,self.high_score_rect)  #将历史最高分绘制在其对应的rect位置上
        self.screen.blit(self.level_image,self.level_rect) #将生于命数（小飞船）绘制在其对应的rect位置上
        
        #绘制剩余命（飞船）
        self.ships.draw(self.screen) 
