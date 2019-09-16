#############   conditional testing条件测试 ############

print('\t####    默认严格区分大小写以及前后空格   ####\n')
car = '1 bmw  2'
print('bmw和 bmw  相等不\n我猜：','bmw' == ' bmw  ')
print('1 BMW  2和1 bmw  2不相等？\n我：','1 BMW  2' != car)
print('1 BMW  2（转小写）和1 bmw  2不相等？\n我：','1 BMW  2（转小写）' != car)


print('\n\n\n\n\t####    如果不区分大小写（先全部转小写比较）   ####\n')
car = ' bmw  '
print('BMW和bmw  相等不\n我猜：',' BMW  '.lower() == car.lower())

if 10 > 9 - 1 and 8<  \
12 and \
2   **   3 == 8 \
or 0:
    print('可行')
