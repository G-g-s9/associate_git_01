print('###########  列表实操测试 —— 邀请 (邀请我所认识的人参加我的party)  ###########')
'''
背景介绍：
邀请认识的人，参加我的一个聚会
我决定请所有认识的人，但有两个来不了，能来的发出邀请
新认识一个朋友，也邀请了
金费不足，只能邀请两个
保留邀请列表前两个，对其他人说明情况，说声抱歉。并和剩下两位再打声招呼，表示他们还是被邀请的

'''
print('This is an invitation letter.\n\n')
who_I_knew = ['幸运儿01','幸运儿02','幸运儿03','幸运儿MVP','幸运儿05（后.来不了）','幸运儿06','幸运儿07','幸运儿08','幸运儿MVP']
print('who I knew:\n\t',who_I_knew)
print('Total: '+str(len(who_I_knew))+' peraons.')

del who_I_knew[5]				# 06失踪了。注：索引从0开始
who_I_knew.remove('幸运儿03')	# 03被关小黑屋，为世人所遗忘

print('\n\.n.\nwait,wait....')

# ~ print(who_I_knew.pop(3)+'....some people may not make it.╮(╯▽╰)╭ \n\n\nlet me coract it.')	#临时来不了<方案一>：pop弹出。需注意前面删了两个列表元素，索引有变动
unlucker = '幸运儿05（后.来不了）'
who_I_knew.remove(unlucker)
print(unlucker+'....some people may not make it.╮(╯▽╰)╭ \n\n\nlet me coract it.Loading...\n\n\n')	#临时来不了<优化方案二>:remove直接弹出指定值，无需考虑索引

# ~ just again
print('who I knew:\n\t',who_I_knew)
print('Total: '+str(len(who_I_knew))+' peraons.')

numbers_invitated = []		#选中者们的列表。我邀请了所有认识且能来的
print('numbers invitated:\n\t',numbers_invitated)


print('正式开始邀请发起:\n\n空表开始填写。。。')
number = []				#空白邀请函（待添加）
# ~ print(len(who_I_knew))     #剩余人数（注释化
for a in range(len(who_I_knew)):	#一个个从上个列表中取出，放入邀请函（相当于逆序拷贝）a从0，1，2，3，4，5，逐一增大到长度6停止
	number.append(who_I_knew.pop())
number.reverse()		#反序排列，破坏原始排序。相当于弹栈之后（反序）的拨正
###接下去欢迎一下
for tmp in number:
	print('dear '.title()+tmp.title()+','+'Welcome to my party.')
print("It's my pleasure to invite you.")


####追加   新认识一位朋友####
new_frend = 'son'.title()
# ~ number.append(new_frend)		#邀请人加入新朋友 方案一，加到末尾
number.insert(2-1,new_frend)		#邀请人加入新朋友 方案二，插到第二位。影响后续只留前两位的决定
# ~ number[2-1] = new_frend		#邀请人加入新朋友 方案三，替换掉第二位。影响后续只留前两位的决定，但这个方案这里语境说不同，弃置


print('\n\n\Lucky gay.I just made a frend,'+new_frend+'.')		#追加说明，并发出邀请
print('\ndear '.title()+new_frend+','+'Welcome to my party.')

print('new invitation list:'.title(),number)	#用逗号是因为number不是str，无法用+相连


print('''\n\n\n\nEmbarrassing,some bad news for us.	
Lack of funding.
I have to invite zhe first two first.Sorry.\n''')	#解释说明原因

Acceptable_figures = 2
print(len(number))
for b in range(len(number)-Acceptable_figures):			#逐一打声招呼，说下抱歉
	print('Sorry '+number.pop()+'.')
print('The above '+str(b+1)+" frends,I'll invita you next time.")


#再次邀请剩下2位
print('\n\n\n')
for b in range(Acceptable_figures):
	print('Congratulation,you have received my invitation,you will continue to attend my party,'+number.pop())
# ~ print(number)	#核实都通知完了，列表空了
# ~ print('In the end,there were only ',b+1+1,'people at my party,including me.')	#算上我
print('In the end,there were only ',b+1,'people at my party besides me.')	#不算我

