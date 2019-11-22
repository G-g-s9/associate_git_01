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
a = a_x,a_y = 600,800
print(a)
print(a_y)


#导入pygame库
import pygame
#导入pygame所有的参数
from pygame.locals import *
#初始化pygame
pygame.init()
#获取对显示系统的访问，并且建立一个窗口，决定分辨率，窗口的宽度和高度写在圆括号中
screen=pygame.display.set_mode((600,500))
#接下来是打印文本的操作
#pygame支持pygame.font将文本输出到图形窗口，要绘制文本，必须先创建一个字体对象
#可以向pygame.font.Font()构造函数提供一个TrueType字体，但是，使用不带引号的None会导致使用默认的pygame字体，这里的pygame字体大小为60
myfont=pygame.font.Font(None,60)
white=255,255,255
blue=0,0,255
textImage=myfont.render("Hello Pygame",True,white)
#上面的操作是将文本提前渲染到一个图像上，textImage对象是可以使用screen.blit（）绘制的平面，第一个参数是文本信息，第二个参数是抗锯齿字体的一个标志（为了提高质量），第三个参数是颜色（一个RGB值）
#要绘制文本，通常的过程是要清除屏幕，进行绘制，然后刷新显示，下面是这三个操作的代码：
screen.fill(blue)

screen.blit(textImage,(100,100))

pygame.display.update()
