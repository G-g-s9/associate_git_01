'''
游戏主文件，其他文件都直接间接被导入这里调用
'''
import pygame       # 导入pygame模块
            # 上面标准库类的
            # 下面自定义类的
from settings import Settings       # 导入settings.py模块中的Settings类
from ship import Ship       # 导入ship.py模块中的Ship类
import game_functions as gf     # 导入game_functions.py模块，名称简化为gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()   # 调用pygame正常工作,这一条必加
    ai_settings =Settings() # 调用类设置实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))     # 建立给screen，宽、高为文件Settings中对应值
    pygame.display.set_caption("Alien Invasion      中文名：外星人入侵")    # 标题换不了行呢

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)      #''' 注意这里我飞船的变量名，后面要不同于教程尝试一下'''

    # 开始游戏主循环.(没有触发 SystemExit 异常来退出程序,就无限刷新)
    while True:

        gf.check_events(ship)    # 监视键盘和鼠标
        ship.update()
        # 每次循环都重绘屏幕 | 填充指定RGB值的颜色 | 让最经绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship)

run_game()
