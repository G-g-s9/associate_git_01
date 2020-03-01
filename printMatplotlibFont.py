#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
这个要进一步看看
https://www.jianshu.com/p/8c51b11e3662
显示一些matplotlib的信息，如 可用字体、缓存目录等
'''
from matplotlib.font_manager import FontManager
import subprocess
import matplotlib    
print('显示matplotlib字体路径\n'+matplotlib.matplotlib_fname()+'\n')

print(matplotlib.get_backend()) #返回matplotlib后端
print(matplotlib.get_cachedir())    #缓存目录
print(matplotlib.get_configdir())   #配置目录
print(matplotlib.get_data_path())   #数据目录
print(matplotlib.get_home())    #用户目录

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
# ~ print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
# ~ print( '*' * 10, '系统可用的中文字体', '*' * 10)
# ~ print (output)
zh_fonts = set(f.split(',', 1)[0] for f in output.decode('utf-8').split('\n'))
available = mat_fonts & zh_fonts
print ('*' * 10, '可用的字体', '*' * 10)
for f in available:
     print (f)
