import pygame
import sys

class Pic():
    """素材图"""
    def __init__(self):
        '''
        素材 大小、方向、不透明杜、
        模糊度（或动态）、色温、层级（可选）、
        显示时间、fps、
        '''
        self.pic = pygame.image.load("alien_invasion/images/alien.png")
        #大小
        self.pic_rect = self.pic.get_rect()

class Screen():
    '''基本无变化的'''
    def __init__():     #基本属性
        self.screen_main_size = (800,800)
        self.screen_main = pygame.display.set_mode(screen_main_size)
        self.pygame.display.set_caption("随机大小、随机分布")
        self.screen_main.fill(134,174,177)

def play():
    '''单一素材图的随机分布主函数'''
    screen = Screen()

    if pygame.get_event() == pygame.QUIT:
        sys.exit()

    pygame.display.flip()
