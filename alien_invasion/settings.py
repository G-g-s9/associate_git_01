class Settings():
    '''存储《外星人入侵》的所有设置'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 900     # 宽数值
        self.screen_height = 600        # 高数值
        self.bg_color = (7,173,187)   # 背景色 RGB值 青绿

        # 飞船设置
        self.ship_speed_factor = 1.4    # 设置飞船速度因素值
