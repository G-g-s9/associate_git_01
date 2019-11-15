import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((900,600))     # 教程里的是元组（1200，800）
    pygame.display.set_caption("Alien Invasion")
    
    # 设置背景色
    bg_color = (7,173,187)
    
    # 开始游戏主循环
    while True:
        
        # 监视键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 每次循环都重绘屏幕
        screen.fill(bg_color)           # 填充指定RGB值的颜色
                
        # 让最经绘制的屏幕可见
        pygame.display.flip()
        
run_game()        
