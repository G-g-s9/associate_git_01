with open('pi_digits.txt') as file_object:  # 相对路径。本程序同目录下文件
    contents =file_object.read()        
    print(contents)

print("---------------------")

# ~ with open('/home/e/桌面/projects_new_start/不熟悉的专有名词积累.txt') as file_object:
with open('/home/e/桌面/projects_new_start/__pycache__/.gitignore') as file_object:
    contents =file_object.read()
    print(contents.rstrip())

print("---------------------")

filename = "global_variable.py"
with open(filename) as file_object:
    for line in file_object:
        print(line,end="")      # 消除多余换行

print("---------------------")

filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()         # 源文件按行输出为 以每行为元素的列表
    
pi_string = ""              # 每行元素拼接
for line in lines:
    pi_string +=line.strip()
    
print(pi_string)
print(len(pi_string))
print("---------------------")
