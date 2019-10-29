# ~ 全局变量
gl_name = "G-g-s9"
class Car():
    """ 一次模拟汽车的简单尝试 """
    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make9 = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """ 返回整洁的描述性信息 """
        long_name = str(self.year) + ' ' + self.make9 + ' ' + self.model
        return long_name.title()
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
