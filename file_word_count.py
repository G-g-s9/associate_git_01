def count_words(filename):      # 拆分计数的自定义函数
    '''
    功能：计数 文件中 词汇/短语
    （目前还不智能，仅能拆分 以换行符、空格、Tab为分隔符的非空片段）    
    '''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        message = "不好意思，没找到 "+filename+" 这个文件。麻烦您重新核实一下文件名\
                    (也可能文件移动或删除了)。\n"
        print(message)
    else:
        # 大致计算文件中的总单词数
            words = contents.split()    # 使用split（）方法分解成单词列表
            num_words = len(words)
            print(filename+" 这个文件中,共有 "+str(num_words)+" 个词汇/短语\n")
            # ~ print(words)        # 这行拿来实际看下具体拆分好的列表
            
filenames = ["error.py","function.py","global_variable.py","errhello_pythonor.py",]
for fm in filenames:
    count_words(fm)         # 我去嘞，一开始列表输错成字典，真的看到字典的无序性了


