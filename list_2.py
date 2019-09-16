print('\
\t####  一些列表练习。主要掌握遍历列表、条件检查\n\t注：几个习题中有变量名重复，\
值不要用串\n\n')



'''
5-8  以特殊方式跟管理员打招呼 ：创建一个至少包含 5 个用户名的列表，且其中一个用户名为
 'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问
候消息。遍历用户名列表，并向每位用户打印一条问候消息。
如果用户名为 'admin' ，就打印一条特殊的问候消息，如 “Hello admin, would you 
like to see a status report?” 。
否则，打印一条普通的问候消息，如 “Hello Eric, thank you for logging in again” 。
'''
print('\n\n\
5-8  \
')
member_of_pc = [ '1号','2号','3号', 'admin','44号','5号']
print(member_of_pc)
for memb in member_of_pc:
    if memb == 'admin':
        print(memb+'这个权限最高呢')
    else:
        print('Hello '+memb+',thank you for logging in again')


'''
5-9  处理没有用户的情形 ：在为完成练习 5-8 编写的程序中，添加一条 if 语句，
检查用户名列表是否为空。
如果为空，就打印消息 “We need to find some users!” 。
删除列表中的所有用户名，确定将打印正确的消息。
'''
print('\n\n\
5-9  \
')
member_of_pc = [ '1号','2号','3号', 'admin','44号','5号']
print('...\nclean all\n\n')
for a in range(len(member_of_pc)):
    member_of_pc.pop()
print(member_of_pc)                         # 看下是不是真空（ / ～ \ ）
# ~ member_of_pc.append('强势插入测试')       # 测试用，默认注释化
if member_of_pc:
    for memb in member_of_pc:
        print(memb+'clean error')
else:
    print('We need to find some users!')



'''
5-10  检查用户名 ：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
创建一个至少包含 5 个用户名的列表，并将其命名为 current_users 。
再创建一个包含 5 个用户名的列表，将其命名为 new_users ，并确保其中有一两个用户名也包
含在列表 current_users 中。
遍历列表 new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一
条消息，指出需要输入别的用户名；否则，打印一条消息，指
出这个用户名未被使用。
确保比较时不区分大消息；换句话说，如果用户名 'John' 已被使用，应拒绝用户名 'JOHN' 。
'''

print('\n\n\
5-10  \
')
current_users = \
                [ '11号','21号','13号',\
                'aD','404DAXIE号','25号']    # 假设库列表
                
# 建立一个小写列表副本，用来查重用(变量名有待优化）
current_users_copy = current_users[:]   # 注意用切片复制，不然就只是关联两个
copy_number_flag = len(current_users)-1
for tmp in current_users_copy:
    current_users_copy[copy_number_flag] = current_users_copy\
    [copy_number_flag].lower()
    copy_number_flag = copy_number_flag-1
print(current_users_copy)

# 👇录入新名查重
new_users = [ '11号','49','88', 'Ad','66','2']
for user in new_users:
    if user.lower() in current_users_copy:
        print('提示： '+user+' 重名，请重命名\n\tPlease rename!')
    else:
        print(user+'\t可使用')
        
# ~ print('\n\n\n',current_users)   # 人工对照用，默认注释化
# ~ print('\n\n\n',current_users_copy)
# ~ print('\n\n\n',new_users)



'''
5-11  序数 ：序数表示位置，如 1st 和 2nd 。大多数序数都以 th 结尾，只有 1 、 2 和 
3 例外。
在一个列表中存储数字 1~9 。
遍历这个列表。
在循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。输出内容应为 1st 、 
2nd 、 3rd 、 4th 、 5th 、 6th 、 7th 、 8th 和 9th ，但每个序
数都独占一行。
'''
print('\n\n\
5-11  \
')
#变量名是拼音哦
shuzi = [1,2,3,4,5,6,7,8,9]
print(shuzi)
xushu = shuzi[:]

tmp = 0
for a in range(0,len(shuzi)):
    if tmp == 0:
        xushu[tmp] = str(xushu[tmp])+'st'
        print(xushu[tmp])
        tmp = tmp + 1
    elif tmp == 1:
        xushu[tmp] = str(xushu[tmp])+'nd'
        print(xushu[tmp])
        tmp = tmp + 1
    elif tmp == 2:
        xushu[tmp] = str(xushu[tmp])+'rd'
        print(xushu[tmp])
        tmp = tmp + 1
    else:
        xushu[tmp] = str(xushu[tmp])+'th'
        print(xushu[tmp])
        tmp = tmp + 1
        
