'''tmp 随用随删'''

        
a,b,c,d = 'wo ',9,4,4+9j
print(type(d))

# ~ filename = "pi_digits.txt"              # 测试附加内容。每次运行都会添加一次
# ~ with open(filename,'a') as file_object:
    # ~ file_object.write("hahhahah")



import json

numbers = [3,4,6,5,8]

filename = "numbers.json"
with open(filename,"w") as f:       # 新建一个json文件，把数组方进去
    view1 = json.dump(numbers,f)            # 转储数据

with open(filename) as t:
    view2 = json.load(t)
    
print(view1)
# ~ print(view2)
    
