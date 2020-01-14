import pygame
import sys

'''
        素材 大小、方向、不透明杜、
        模糊度（或动态）、色温、层级（可选）、
        显示时间、fps、
        '''



def run():
    '''主程序：单一素材图的随机分布主函数'''
    pygame.init()   # 调用pygame正常工作,这一条必加
    screen_main_size = (800,800)
    screen_main = pygame.display.set_mode(screen_main_size)
    screen_main_rect = screen_main.get_rect()
    pygame.display.set_caption("随机大小、随机分布")

    pic = pygame.image.load("alien_invasion/images/alien.png")
    pic = pygame.transform.scale(pic,(49,49))
    pic_rect = pic.get_rect()

        
    while True:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                sys.exit()

        screen_main.fill((255,255,255))
        
        #测试位置
        dest = pic_rect
        dest.bottom =screen_main_rect.bottom
        screen_main.blit(pic,dest)
        pygame.display.flip()
run()
