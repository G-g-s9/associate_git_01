'''
游戏主文件,其他文件都直接间接被导入这里调用
'''
import pygame       # 导入pygame模块
from pygame.sprite import Group   #编组容器类模块
            # 上面标准库类的
            # 下面自定义类的
from settings import Settings       # 导入settings.py模块中的Settings类
from ship import Ship       # 导入ship.py模块中的Ship类
# ~ from alien import Alien       # 导入alien.py模块中的Alien类
import game_functions as gf     # 导入game_functions.py模块,名称简化为gf
from game_stats import GameStats    #活动标签和统计信息
from scoreboard import Scoreboard   #记分牌——统计数据显示
from button import Button       # 导入button.py模块中的Button类



def run_game():
    '''运行主函数,简洁些'''
    # 初始化游戏并创建一个屏幕对象
    pygame.init()   # 调用pygame正常工作,这一条必加
    ai_settings =Settings() # 调用类设置实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))     # 建立给screen,宽、高为文件Settings中对应值
    pygame.display.set_caption("Alien Invasion    中文名：外星人入侵(按【q】可退出)")    # 标题换不了行呢

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    
    #记分牌
    sb = Scoreboard(screen,ai_settings,stats)

    # 创建Play按钮
    play_button = Button(screen,"开始游戏 | Play")     #试了几个常用字体，就苹方能正常显示中文

    #创建一个时间对象
    fps = 1000    #帧率参数，一般1000
    clock = pygame.time.Clock()   #创建一个时间对象clock

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)      #''' 注意这里我飞船的变量名,后面要不同于教程尝试一下'''

    # 创建一个用于存储有效子弹的编组
    bullets = Group()   #一个空子弹集

    # 创建一个存储外星人群的编组
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)    # 外星人群

    # 开始游戏主循环.(没有触发 SystemExit 异常来退出程序,就无限刷新)
    while True:

        gf.check_events(ai_settings,screen,ship,bullets,stats,
                        play_button,aliens,sb)    # 监视键盘和鼠标

        if stats.game_active == True:
            ship.update()   #刷新飞船
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship,
                                stats,sb)    #刷新屏幕子弹集
            gf.update_aliens(stats,aliens,bullets,ai_settings,screen,ship,sb)    #刷新整个alien_fleet集

        # 每次循环都重绘屏幕 | 填充指定RGB值的颜色 | 让最经绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,
                        play_button,sb)

        clock.tick(fps)   #每帧调用，计算上次调用到这次的毫秒数

run_game()
