def make_pizza(size, *toppings):
    """ 概述要制作的比萨 """
    print("\n做一个 " + str(size) +
    "-寸批萨，要包含以下食材:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese','green peppers')

import global_variable
print(global_variable.gl_name)


"""测试字典输出顺序"""
jihe={}
jihe["键名1"]="啦啦啦1"
jihe["键名2"]="啦222"
jihe["键名3"]=3
jihe["键名4"]="丝丝"

for c,d in jihe.items():
    print(c,d)

print("\n\n\n\n")

"""测试字典输出顺序"""
jihe={
    "键名3":3,
    "键名4":"丝丝",
    "键名1":"啦啦啦1",
    "键名2":"啦222",
    
    }

for c,d in jihe.items():
    print(c,d)


from collections import OrderedDict

gg=OrderedDict()

gg[3]=6
gg[2]=8
gg[4]=2
gg[9]=3

for c,d in gg.items():
    print(c,d)


d1 = {'a':1,'c':4,'b':2,'d':3}
d2 = {2:1,3:4,4:2,1:5,5:3}
d3 = {
    '01': {'name': '电脑', 'price': 3000}, 
    '02': {'name': '鼠标', 'price': 50}, 
    '03': {'name': '洗发水', 'price': 30}, 
    '04': {'name': '微波炉', 'price': 998},
    '05': {'name': '手机', 'price': 1500}
     }
     

     
for c,d in sorted(d1.items(),key = lambda x:x[0],reverse = True):
    print(c,d)  # 键名逆序


# ~ for c,d in sorted(d.items(),key=lambda x:x[1]['price']):    # 嵌套字典排序失败
    # ~ print(c,d)
