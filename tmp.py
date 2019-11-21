'''tmp 随用随删'''


a,b,c,d = 'wo ',9,4,4+9j
print(type(d))

# ~ filename = "pi_digits.txt"              # 测试附加内容。每次运行都会添加一次
# ~ with open(filename,'a') as file_object:
    # ~ file_object.write("hahhahah")


c = "jkjkjkJ"
print(c.count("j"))
print(c.lower().count("j"))
# ~ print(c.count("j").lower())         # 错误代码，属性是从左到右的


import json

numbers = [3,4,6,5,8]

filename = "numbers.json"
with open(filename,"w") as f:       # 新建一个json文件，把数组方进去
    view1 = json.dump(numbers,f)            # 转储数据

with open(filename) as t:
    view2 = json.load(t)

print(view1)
# ~ print(view2)

dict = {'Name': 'Runoob', 'Age': 27}
print ("Age 值为 : ",dict.get('Age'))


print(str({'google': 'google.com', 'runoob': 'runoob.com'}),"\n\n\n\n")


#####################################

import pygame
pygame.init()

screen = pygame.display.set_mode(
        (400,400))

while True:
    if input()=='q':
        break
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                x = event.key
            print(str(x))
