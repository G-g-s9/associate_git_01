
# -*- coding: utf-8 -*-
#	上面这句是使本脚本使用 unicode UTF-8 编码,支持多国语言（绝大多数吧，目前我还不知道是哪些）

'''
****本文件作用声明****
作为快速学习用，杂糅知识点记录（部分小测试代码）
先有个系统印象和概念，同时培养兴趣
到第二部分项目再仔细回顾知识点（可适当系统回顾）
'''

print('\n\t### -*-  开始掌握吧，少年 -*- ### ')
#	各种注释表示，#、‘、’‘、’‘’、\rddfd
'''
方法(紧跟变量后）
是 Python 可对数据执行的操作。
在 name.title() 中， name 后面的句点（ . ）让 Python 对变量 name 执行方法 title() 指定的操作。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成
其工作。这种信息是在括号内提供的。函数 title() 不需要额外的信息，因此它后面的括号是空的
title()首字母大写，其余小写	；	upper()全部大写	；	lower()全部小写

'''

#	+ 字符串直接拼接，必须都是字符型。扩展str()函数

#	 rstrip()右侧（末尾）开始删多余空格	；	 lstrip()左侧（开头）开始删多余空格	；	 strip()两端开始删多余空格

'''
\r

				转移符
#		\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\xff	十六进制数，ff代表的字符，例如：\x0a代表换行	这里不用yy是debug
\other	其它的字符以普通格式输出

'''

# ~ print('\t使用快捷ctrl+e，让选中code disable(代码前面会多出 # ~ )')

'''

#	pond character英镑符  /  octothorpe八角帽
+	plus
-	minus
/	slash  （\ back slash）
*	asterisk		**为乘方
%	percent
<	less-than
>	greater-than
<=	less-than-equal
>=	greater-than-equal
下面是运算符测试——数鸡
'''
print('\n\n\t\
###############  数 鸡  ####################\
\n\t')

print('I will now count my chickens')
print("hens",25 + 30 / 6)	#母鸡
print('roosters',\
100 - 25 * 3 % 4)		#公鸡	中间的内容可以用","连接字符串和数字，不过输出有空格间隔（逗号位置） ； \backslash 续行符
print('Now I will count the eggs:')
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print('Is it true that 3 + 2 < 5 - 7?')
print(3 + 2 < 5 - 7)
print('What is 3 + 2?', 3 + 2)
print('What is 5 - 7?', 5 - 7)
print("Oh,that's why it's False.")
print('How about some more.')
print('Is it greater?', 5 > -2)
print(   'Is it greater or equal?'  ,         5   >= -2   , "    	 乱入测空格")	#逗号前后的项默认去多余空格，类似strip()
print('Is it less or equal?', 5 <= -2)

print('\n\t\
###############  数鸡_OVER  ####################\
\n\t')



print('\n\t\
###############  列表学习  ####################\
\n\t')

'''

列表
[<元素值>,<元素值>,<元素值>]		#元素值必须是确实有的。如‘字符串’

*********索引0开头，必须是int，而元素值类型不一定统一**********

.append(<元素值>)	#方法；堆栈形式的添加到末位，-1
.insert(<索引>，<元素值>)	#方法；指定位置插入
del <具体索引>	#语句；指定位置删除，后面元素集体左移一位
.pop（<索引>）	#方法；弹出（无传参时，默认最后一个）指定位置值，需立即赋值用掉（存储），不然就丢了
.remove(<索引>)	#方法；移除指定值（需注意的是只删除第一个出现的该值）
.sort（）/.sort（reverse=True）		#方法；按字母顺序/逆序排列，破坏原始排序
sorted（）			#函数；相当于临时排序输出，源列表排序不动
.reverse()		#方法；直接当前列表反序

'''


print('\n\n\n\n')
import this				#导入Python之禅，即提倡的编程理念
import keyword			#python默认关键字
b = keyword.kwlist		#将 关键字列表 赋值 给变量 b
# ~ 杂
print(b,'\n\n\n')
print('最后一个关键字是：',b[-1],'\n\n')			

null_received = []
x=1
null_received.append(x)				#方法.append：列表末尾插入新元素
print('null_received:',null_received,'\nThe last member of null_received:',null_received[-1])
'''☝比较下 直接输出列表 与 输出列表里的值 ，展示形式不同'''

null_received.append('1')
print(null_received[0]==null_received[1])	#比较两个1是否相同。不同
print(type(null_received[0]),type(null_received[1]))	#输出类型 int str
print(isinstance(null_received[0],(int,str)))		#比较列表第一个值是不是元组中两个类型中的一个。 是的
print(isinstance(null_received[1],int))
print(null_received)
del null_received[0]				#del语句，删除
print(null_received)


print('\n\t\
###############  列表over  ####################\
\n\t')

print('\n\t\
###############  PEP 8  代码格式规范  ####################\
\n\t')
a_tmp_number_tuple = (1,2,6,' ',6,5,		#哈～这里试的元组
					 8,6,57,8,9)
print(a_tmp_number_tuple)


a_tmp_number_list = [1,2,6,' ',6,5,8,		#列表试试,结果一样
					6,57,8,9]
print(a_tmp_number_list)



print("学号\t姓名\t语文\t数学\t英语")
print("2019001\t曹操\t99\t88\t0")
print("2019002\t周瑜\t92\t45     \t93")		# ？5个空格不超制表符
print("2019008\t黄盖\t77\t\t82\t\t100")


print('你好吗？\r朋友')		# 	换行光标停在上一行，再输出后面的，就覆盖掉了一行
# ~ 012345678901234567890123456789012345678901234567890123456789012345678901

print('\n\n****内容分割线****\n\n')

aliens = []     # 创建外星人空列表
for alien_number in range(9):               # 这里直接用循环变量名指出含义
    new_alien = {'color':'green','points':5,'speed':'slow'} # 样例-字典
    aliens.append(new_alien)        #添加到列表
    
for alien in aliens[:4]:        # 展示前4个
    print(alien)
print  ('...')                  # 省略号

print('共创建 '+str(len(aliens))+' 个外星人')

for alien in aliens[:2]:            # 选取前两个绿外星人进化为黄外星人
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['pointa'] = 10
    elif alien['color'] == 'yellow':        # 如果其中有已经变异为黄外星人的
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['pointa'] = 15
    elif alien['color'] == 'red':        # 如果其中有已经变异为黄外星人的
        alien['color'] = 'balck'
        alien['speed'] = 'more fast'
        alien['pointa'] = 25

for alien in aliens[:4]:        # 展示前4个
    print(alien)
print  ('...')                  # 省略号

        
print('\n\n****内容分割线****\n\n')

# ~ 试试字典字典
d1 = {}
d_s1 = {'name':'007','gg':'99','':6}    # 哇塞诶，键名可以空
for value,key in d_s1.items():
    print(value,key)
d1 = {
    'nei':d_s1,
    'ha':d_s1,
    'ho':d_s1,
    }
print(d1)
for value,key in d1.items():
    print('  ',value.title(),key,sep = '\n\t')
        
print('\n\n****内容分割线****\n\n')

name = input('Your name is : ')
print('哦，老铁，原来你就是'+str(name)+'，久仰久仰！失敬失敬！')

number = input('请输入一个数字： ')
print(6.6>6)


print('\n\n****内容分割线****\n\n')


# ~ 要退出吗？_____实际是小代码块，不停问，直到输入quit停止运行
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True       # 活动状态。设个标志来作为枢纽式判断标准
while active :
    message = input(prompt)
    
    if message != 'quit':   # 不是就把输入打印出来
            print(message)
    else:
        active = False#标志取反，循环停止
   
print('\n\n****内容分割线****\n\n')

### 定义函数

def favorite_book(title):
    """显示我最喜欢的书籍名"""
    print(" One of my favorite books is \n"+title.title())
    # ~ print("my name is "+global_variable.gl_name)
    
favorite_book( "Alice in Wonderland")
   
print('\n\n****内容分割线****\n\n')

def make_shirt(size='XL',ppt=''):
    print("a "+size+" T-shirt with "+'"'+ppt+'".')
    
make_shirt(ppt="love".title())
make_shirt('s',ppt="love".title())

