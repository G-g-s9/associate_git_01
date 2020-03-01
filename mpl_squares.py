'''
matplotlib尝试使用
'''
import matplotlib.pyplot as plt #导入matplotlib库中的pyplot模块，并别名plt
# ~ import pylab as plt #等效于上一条
from matplotlib.font_manager import FontProperties  #导入matplotlib库中的字体管理模块

squares = [1,4,9,16,25,36]  #一维数据列表
plt.plot(squares,linewidth=5)   #函数 尝试绘制对应图形 线宽5 确定映射关系


#标题，坐标标签
plt.title('\n\nSquare\n平方数', fontproperties="pingfang",fontsize=24)  #标题 字号24 默认居中
plt.xlabel('Value',fontsize=14) #横坐标标签 字号14
plt.ylabel('Square of Value',fontsize=14)   #纵坐标标签 字号14

#设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)

plt.show()  #打开matplotlib查看器（可操作），并显示绘制好的图形
