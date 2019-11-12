'''简单访客记录;记录文件guest_book.txt'''
'''
    还有3个问题
    
    ⭕总标识数
    
    ⭕关于历史记录表的视觉效果整齐，可选 
    1 限制命名（以最大值为依据调整） 
    2 记录表内命名长的换行
    3 后台不调整（没必要），后面可视化输出再具体优化
    
    ⭕改为模块
    
'''


import time

flag = 0        # 每次运行的标识数
n = 5             # 设每次运行仅录入前5个访客信息
ordin = 1       # 运行的总标识数，现在这个还不是总的,须改正
while flag < n:
    if flag<1:
        print("退出，请按‘q’ ； 清空访客记录，请按‘clear’\n")
    name = input("请输入您的姓名：")
    point = time.strftime('%Y-%m-%d %H:%M:%S %p %a',\
                        time.localtime(time.time()))    # 记录录入时间
    if name =="":
        name = input("姓名不能为空。直接按‘q’可退出\n")
        flag-=1        # 一个问题录入空也计数了，减回来
    elif name =="q":
        flag=n+1        # 退出wile循环条件，当作退出；也可以直接break终止循环
    elif name == "clear":
        '''清空记录'''
        with open('guest_book.txt','w') as file_object:
            point = time.strftime('%Y-%m-%d %H:%M:%S %p %a',\
                                time.localtime(time.time()))    # 记录录入时间
            message = "之前的历史纪录已全清于 "+point+\
                        "\n序号 \t访客    \t操作时间\n"
            file_object.write(message)
        flag=n+1        # 退出wile循环条件，当作退出
    else:
        print("欢迎"+name+"光临本站!")
        with open('guest_book.txt','a') as file_object:
            file_object.write(str(ordin)+'\t'+str(name)+"\t\t"+str(point)+"\n")
    flag+=1
    ordin+=1
