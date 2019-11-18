import sys

import pygame       # 上面标准库类的
                    # 下面自定义类的
from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()   # 调用
    ai_settings =Settings() # ai设置实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))     
    pygame.display.set_caption("Alien Invasion      中文名：外星人入侵")    # 标题换不了行呢
    
    # 设置背景色
    bg_color = (7,173,187)
    
    # 创建一艘飞船
    ship_01 = Ship(screen)
    
    # 开始游戏主循环
    while True:
        
        # 监视键盘和鼠标
        for event in pygame.event.get():        # 这一段还一脸懵比
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 每次循环都重绘屏幕
        screen.fill(bg_color)           # 填充指定RGB值的颜色
        ship_01.blitme()
                
        # 让最经绘制的屏幕可见
        pygame.display.flip()
        
run_game()        
