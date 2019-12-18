class GameStats():
    """一个用于跟踪游戏统计信息的新类"""
    def __init__(self,ai_settings):
        '''初始化属性'''
        self.ai_settings = ai_settings  #传参
        self.reset_stats()  #调用👇下面的重置方法   不直接在__init__内传递值，是让值隶属于本类，而不是实例（待进一步核实）
        self.game_active = False     #游戏活动状态标志,初始值非,等玩家触发

    def reset_stats(self):
        '''初始化游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit   #传参，最初设定的飞船条数
        self.score = 0  #初始积分0  写这里是因为是变量（写在__init__里的初始值都是定值），随游戏进行，后期会变的
