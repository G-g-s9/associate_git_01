class Settings():
    '''存储《外星人入侵》的所有设置,使用类而不是函数,是为了传参'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置-窗口、背景等
        self.screen_width = 900     # 宽数值
        self.screen_height = 600        # 高数值
        self.bg_color = (7,173,187)   # 背景色 RGB值 青绿

        # 飞船设置
        self.ship_speed_factor = 1.4    # 设置飞船速度因素值（接受浮点数,可以相对微调）

        # 子弹设置
        self.bullet_speed_factor = 1    # 设置子弹速度因素值（接受浮点数,默认比飞船速度低,为了游戏操作体验友善些）
        self.bullet_width = 3   # 子弹宽
        self.bullet_height = 10   # 子弹高度
        self.bullet_color = 209,154,88    # 子弹颜色RGB值。暗金
        self.bullets_allowed = 3     # 屏幕内子弹数max
