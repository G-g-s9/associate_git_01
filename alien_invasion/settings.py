class Settings():
    '''
        存储《外星人入侵》的所有设置,使用类而不是函数,是为了传参
        在这里设的值，都可以认为是允许调节的参数，不在这里的一些初始化值就属于程序稳定性要求的定值
    '''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置-窗口、背景等
        self.screen_width = 900     # 宽数值
        self.screen_height = 600        # 高数值
        self.bg_color = (7,173,187)   # 背景色 RGB值 青绿

        # 飞船设置
        # ~ self.ship_speed_factor = 1.4    # 设置飞船速度因素值（接受浮点数,可以相对微调）,移入动态参数里了
        self.ship_limit = 2     # 飞船数量限制（相当于玩家有几条命）;0,1,2,
        self.ship_h = 94        #飞船高

        # 子弹设置
        # ~ self.bullet_speed_factor = 3    # 设置子弹速度因素值（接受浮点数,默认比飞船速度低,为了游戏操作体验友善些）后移入动态参数
        self.bullet_width = 1800   # 子弹宽3,全屏攻击900*2
        self.bullet_height = 10   # 子弹高度
        self.bullet_color = 209,154,88    # 子弹颜色RGB值。暗金
        self.bullets_allowed = 9     # 屏幕内子弹数max

        # 外星人设置
        self.alien_h = 49   # 外星人高
        # ~ self.alien_speed_factor = 1 # 外星人速度因素(接受浮点型)，默认远小于飞船（难度低，上手简单 后移入动态参数中
        self.fleet_drop_speed = 10  # 舰队向下闪现速度，y方向，碰到屏幕边缘调用
        # fleet_directtion为1表示右移，为-1表示左移
        # ~ self.fleet_direction = 1   # 移动方向 后移入动态参数中

        #控制整体游戏节奏参数
        self.speedup_scale = 1.1        #速度提升比例factor

        self.initialize_dynamic_settings()      #初始化动态设置

    def initialize_dynamic_settings(self):
        '''初始化动态变化设置属性，随游戏变动,这里算是动态参数的初始值'''
        self.ship_speed_factor = 1.4    # 设置飞船速度因素值（接受浮点数,可以相对微调）
        self.bullet_speed_factor = 3    # 设置子弹速度因素值（接受浮点数,默认比飞船速度低,为了游戏操作体验友善些）
        self.alien_speed_factor = 1 # 外星人速度因素(接受浮点型)，默认远小于飞船（难度低，上手简单

        #外星人横向移动方向，1向右，-1向左
        self.fleet_direction = 1   # 移动方向

    def increase_speed(self):
        '''提速部分.所有速度因素都乘以提升比例'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
