'''

空格不影响 Python 计算表达式的方式，它们的存在旨在让你阅读代码时，能迅速确定先执行哪些运算

'''

anser1=3+3
print('3+3=\b')
print(anser1)				#浮点型问题，结果包含的小数位数可能是不确定的
print(0.1+0.2)			#暂时忽略多余的小数位数即可；在第二部分的项目中，你将学习在需要时处理多余小数位的方式


for value in range(-5,5):
	print(value)

squares = []				#由1~10的平方值组成的一个列表
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)

#fab 0 1 1 2 3 5 8...
print('\n\n\n************输出Fibonacci Sequence(斐波那契数列)的前20个值\n')
fab_20 = [0,1]
for i in range(0,20):
	fab = fab_20[i]+fab_20[i+1]
	fab_20.append(fab)
print(fab_20)

print(min(fab_20))			#输出数列中的最小值
print(max(fab_20))			#输出数列中的最大值
print(sum(fab_20))			#输出数列元素之和

print('\n\n\n************输出1-100 0000的累加值\n')
sub_sum = []
for s in range(0,1000001):
	sub_sum.append(s+1)
print(sum(sub_sum))


print('\n\n\n************输出1-20内的奇数(已知规律,输出列表)\n')
odd_number_20 = []
for odd in range(1,21,2):
	odd_number_20.append(odd)
print(odd_number_20)

print('\n\n\n***********输出1-10立方组成的数列\n')
cube = []
for cu in range(1,11):
	print(cu**3)

print('\n\n\n***********输出1-10立方组成的数列（用列表解析方式，输出列表即可\n')
cube_method_02 = [cu**3 for cu in range(1,11)]		#列表解析
print(cube_method_02)

print('\n\n\n***********输出2-5切片:\n')				#切片
print('\t\t',cube_method_02[1:5])
print('省略切片要求输出：',cube_method_02[:])

print(2**100)

print('\n\n\n\n\n#############获取时间戳')
import time				
print(time.time())

print('\n\n\n\n\n#############排序测试数字')
sort_tmp_list=[56,67,1,39,59]		
print('\n原列表:',sort_tmp_list)
print('排序后:',sorted(sort_tmp_list))

print('\n\n\n\n\n#############排序测试-字母数字混合')
sort_tmp_list=['n_56','a_67','N__1','文_39','阿_59']		
print('\n原列表:',sort_tmp_list)
print('排序后:',sorted(sort_tmp_list))

print('\n\n\n\n\n#############排序测试-中文')
sort_tmp_list=['文章','阿语','心静','阿六','阿5']		
print('\n原列表:',sort_tmp_list)
print('排序后:',sorted(sort_tmp_list))


print('\n\n\n\n\n#############tuple')
sort_tmp_list=(' ','阿语','心静','阿六','阿5')	
print('\n原列表:',sort_tmp_list)
print(sort_tmp_list[3])
sort_tmp_list[3] = '3'
print('排序后:',sorted(sort_tmp_list))




