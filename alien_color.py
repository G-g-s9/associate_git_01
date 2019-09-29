import random

print('\t#*  夏季把乱扯 的死亡外星人颜色  *#\n\n')

#先颜色属性列表
alien_colors = ['green','yellow','blue','red']

#玩家列表
user_names = ['player_01','player_02','player_03','lucky gay',\
             'player_05',\
             'player_06',]
             
#随即抓一个玩家
ran = int(random.random()*6)    #随机数0、1、2、3、4、5
print('随即编号（抽取）为：'+str(ran+1))    # 编号=随机数加一
print('这位玩家是:'+user_names[int(ran)])

#积分初始值
integral = 0
#遍历颜色（这里直接跳过了过程，光输出符合元素，人员随机抽取）
for dead_alien in alien_colors:
    if dead_alien == 'green':
        integral_g = integral+5
        print('congratulations! '.title()+user_names[ran].title()+\
        ' was dead.You current score is '+str(integral_g)+'.\n')
    elif dead_alien == 'yellow':
        integral_r = integral+444
        print('黄色👽'.title()+user_names[ran].title()+\
        ' 得积分'+str(integral_r)+'.\n')    
    elif dead_alien == 'red':
        integral_r = integral+999
        print('厉害了！老铁 全服通告：'.title()+user_names[ran].title()+\
        ' 超神，一刀获得积分'+str(integral_r)+'.')
        
print('\n\n\n\#####delimiter:######（未完待续...）')
print(random.random()*4)
