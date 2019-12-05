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
        self.ship_limit = 3     # 飞船数量限制（相当于玩家有几条命）;0,1,2,3

        # 子弹设置
        self.bullet_speed_factor = 3    # 设置子弹速度因素值（接受浮点数,默认比飞船速度低,为了游戏操作体验友善些）
        self.bullet_width = 3   # 子弹宽
        self.bullet_height = 10   # 子弹高度
        self.bullet_color = 209,154,88    # 子弹颜色RGB值。暗金
        self.bullets_allowed = 9     # 屏幕内子弹数max

        # 外星人设置
        self.alien_h = 29   # 外星人高
        self.alien_speed_factor = 1 # 外星人速度因素(接受浮点型)，默认远小于飞船（难度低，上手简单
        self.fleet_drop_speed = 140  # 舰队向下闪现速度，y方向，碰到屏幕边缘调用
        # fleet_directtion为1表示右移，为-1表示左移
        self.fleet_direction = 1   # 移动方向

        # 彩蛋——可爱的monster团子，预计给玩家惊喜
        # ~ self.lovely = pygame.image.load("images/monster.png")

