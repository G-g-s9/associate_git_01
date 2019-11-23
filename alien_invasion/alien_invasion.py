'''
游戏主文件,其他文件都直接间接被导入这里调用
'''
import pygame       # 导入pygame模块
from pygame.sprite import Group   #编组容器类模块
            # 上面标准库类的
            # 下面自定义类的
from settings import Settings       # 导入settings.py模块中的Settings类
from ship import Ship       # 导入ship.py模块中的Ship类
import game_functions as gf     # 导入game_functions.py模块,名称简化为gf

def run_game():
    '''运行主函数,简洁些'''
    # 初始化游戏并创建一个屏幕对象
    pygame.init()   # 调用pygame正常工作,这一条必加
    ai_settings =Settings() # 调用类设置实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))     # 建立给screen,宽、高为文件Settings中对应值
    pygame.display.set_caption("Alien Invasion      中文名：外星人入侵")    # 标题换不了行呢

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)      #''' 注意这里我飞船的变量名,后面要不同于教程尝试一下'''

    # 创建一个用于存储有效子弹的编组
    bullets = Group()   #一个空子弹集

    # 开始游戏主循环.(没有触发 SystemExit 异常来退出程序,就无限刷新)
    while True:

        gf.check_events(ai_settings,screen,ship,bullets)    # 监视键盘和鼠标
        ship.update()   #刷新飞船
        bullets.update()    #刷新子弹

        #删除飞出屏幕的子弹
        for bullet in bullets.copy():   # 复制组
            if bullet.rect.bottom <= 0:     # 判断子弹的底部已不在屏幕内
                bullets.remove(bullet)      # 将该子弹从子弹集删除
        print(len(bullets))         # 后台实时显示子弹集元素个数

        # 每次循环都重绘屏幕 | 填充指定RGB值的颜色 | 让最经绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
