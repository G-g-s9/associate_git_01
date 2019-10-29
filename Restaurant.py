class  Restaurant():
    '''餐馆尝试'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化描述餐馆'''
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        '''显示简介'''
        print(self.name.title()+"\n是一家擅长"+self.type+"的特色店")
    def open_restaurant(self):
        '''状态'''
        print("尊敬的 Master，欢迎来到 "+self.name.title()+
              " 小的们正等着您呢！")
    def set_number_served(self,x_number):
        '''手动设置就餐人数'''
        self.number_served=x_number
    def increment_number_served(self,incre_number):
        '''预计每日就餐人数,手动加的一个递增值，操作员自定'''
        self.number_served+=incre_number
        print("又有 "+str(incre_number)+"位顾客光临\n当前就餐人数为： "+
                str(self.number_served))

restaurant=Restaurant("小四川","川菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(6)
restaurant.increment_number_served(9)
restaurant.set_number_served(4)
print("目前店里有 "+str(restaurant.number_served)+"位顾客正在就餐。")

