import sys

import pygame

from ship import Ship

def check_events():
	'''响应按键和鼠标时间'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:		# 单击窗口关闭按钮时，将检测到 pygame.QUIT 事件
			sys.exit()		# 触发 SystemExit 异常来退出程序

def update_screen(ai_settings,screen,ship_01):
    '''更新屏幕图像，并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship_01.blitme
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    
