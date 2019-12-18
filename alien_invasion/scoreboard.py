import pygame.font

class Scoreboard():
    '''记分板，显示得分信息的类'''

    def __init__(self,screen,ai_settings,stats):
        '''初始化值，各种得分相关值'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息的字体设置
        self.text_color = (255,0,0)
        self.font = pygame.font.Font('font/pingfang.ttf',48)

        #准备初始得分图像
        self.prep_score()

    def prep_score():
        '''得分信息渲染'''
        score_str = str(self.stats.scre)
        self.score_image = self.font.render(score_str,True,self.text_color,
                                            self.ai_settings.bg_color)

        #将得分放在屏幕右上角

