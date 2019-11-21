import sys          # 导入sys模块（这里退出程序用）

import pygame       # 导入pygame模块

def check_keydown_events(event,ship):
    '''响应按下的函数'''
    if event.key == pygame.K_RIGHT:    # 判断为方向右移键
        ship.moving_right = True    # 右移标记为真
    elif event.key == pygame.K_LEFT:    # 判断为方向左移键   这里可以用 elif是因为每个按下时间都会判断一次，同时按键两个键都会被识别出来
        ship.moving_left = True    # 左移标记为真

def check_keyup_events(event,ship):
    '''响应弹起的函数'''
    if event.key == pygame.K_RIGHT:    # 判断为方向右移键
        ship.moving_right = False    # 右移标记为假
    elif event.key == pygame.K_LEFT:    # 判断为方向左移键
        ship.moving_left = False    # 左移标记为假

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():        # 有事件发生就进入for循环
        if event.type == pygame.QUIT:       # 点击窗口关闭按钮，将检测到 pygame.QUIT 事件
            sys.exit()      # 触发 SystemExit 异常来退出程序

        elif event.type == pygame.KEYDOWN:  # 触发按键事件（按下）
            check_keydown_events(event,ship)    # 跳转到按下响应函数

        elif event.type == pygame.KEYUP:    # 触发按键弹起
            check_keyup_events(event,ship)  # 跳转到按键弹起响应函数

def update_screen(ai_settings,screen,ship):
    '''更新屏幕图像，并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)    # 填充色
    ship.blitme()   # 在指定位置绘制飞船
    # 让最近绘制的屏幕可见
    pygame.display.flip()

