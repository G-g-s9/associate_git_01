'''tmp 随用随删'''

        
a,b,c,d = 'wo ',9,4,4+9j
print(type(d))

# ~ filename = "pi_digits.txt"              # 测试附加内容。每次运行都会添加一次
# ~ with open(filename,'a') as file_object:
    # ~ file_object.write("hahhahah")

filename =  "不熟悉的专有名词积累.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    message = "不好意思，没找到 "+filename+" 文件。麻烦您重新核实一下。\n"
    print(message)
else:
    # 大致计算文件中的总单词数
        words = contents.split()    # 使用split（）方法分解成单词列表
        num_words = len(words)
        print(filename+" 这个文件中,共有 "+str(num_words)+" 个词汇/短语\n")
        # ~ print(words)        # 看了一下，是以换行符、空格、Tab为分隔符，且单独空格认为是空内容不单独记录
