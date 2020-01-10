class GameStats():
    """一个用于跟踪游戏统计信息的类"""
    def __init__(self,ai_settings):
        '''初始化属性'''
        self.ai_settings = ai_settings  #传参
        self.reset_stats()  #调用👇下面的重置方法   不直接在__init__内传递值，是让值隶属于本类，而不是实例（待进一步核实）
        self.game_active = False     #游戏活动状态标志,初始值非,等玩家触发
        
        #最高得分不应被重置，故在此  不过也就在程序没关闭时才有用（后期加个外部文档记录
        
        try:
            with open('high_score_value.txt') as file_object:   #读取文件
                self.high_score = int(file_object.read())     #玩家最高历史得分  
        except ValueError:  #**bug 如果一开始文档内容为空(e..之前不小心写入''报错过）就报错（应该先将初始积分副给历史最高,下面用
            self.high_score = 0

    def reset_stats(self):
        '''初始化游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit   #传参，最初设定的飞船条数
        self.score = 0  #初始积分0  **写这里是因为是变量（写在__init__里的初始值都是定值，固定属性），随游戏进行，后期会变的
        self.level = 1  #初始等级1 和积分类似，可重用
