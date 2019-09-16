'''
方法 是 Python 可对数据执行的操作。
在 name.title() 中， name 后面的句点（ . ）让 Python 对变量 name 执行方法 title() 指定的操作。
每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。
函数 title() 不需要额外的信息，因此它后面的括号是空的
'''
print("##对输入的名字，标准格式化，再输出##\n")
print('first name:\t')
first_name = input()+"(this is first)"  #input用户输入的，电脑就当是字符串
print('last name:\t')
last_name = input()+"LovelAce（这串英文先钉死了）"
full_name = first_name.title().script() + " " + last_name.lower()		#.title()标题 每个单词的首字母强制大写
print(full_name)
