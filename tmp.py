'''tmp 随用随删'''

        
a,b,c,d = 'wo ',9,4,4+9j
print(type(d))

# ~ filename = "pi_digits.txt"              # 测试附加内容。每次运行都会添加一次
# ~ with open(filename,'a') as file_object:
    # ~ file_object.write("hahhahah")


c = "jkjkjkJ"
print(c.count("j"))
print(c.lower().count("j"))
# ~ print(c.count("j").lower())			# 错误代码，属性是从左到右的
