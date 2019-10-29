class Dog():
    """小狗类的尝试——模拟小狗"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" is now rolled over!")


my_dog = Dog('willie',6)        # 创建实例。一只名叫Willie的6岁小狗

print("My dog's name is "+my_dog.name.title() +".")
print("My dog is "+str(my_dog.age)+" years old.")
