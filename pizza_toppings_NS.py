
#批萨点餐

#初始值（份数，后期改为录入）    可选各配料余量（服务员手上，不给顾客看
mushrooms = 9   # 蘑菇9份
green_peppers = 13  # 青椒13份
red_peppers = 6    # 红椒6份
# ~ cucumber = 20   # 黄瓜20份
# ~ tomato = 9  # 番茄🍅9份
# ~ onions = 23 # 洋葱23份
# ~ bacon = 31  # 培根31份
# ~ sausage = 6 # 香肠6份
orleans_drumsticks = 20 # 奥尔良口味鸡腿肉20份
cheese = 40 # 芝士40份

recent_topping_allwance = [mushrooms,green_peppers,red_peppers,\
                          # ~ cucumber,tomato,onions,bacon,sausage,\
                          orleans_drumsticks,cheese]
recent_toppings = ['蘑菇','青椒','红椒',\
                          # ~ '黄瓜','番茄🍅','洋葱','培根','香肠🌭',\
                          '鸡腿肉','芝士']

print('\t**** 配料余量表 ****')
#首行名称
for topping_name in recent_toppings:
    print(topping_name,end='')
    print('\t',end='')
print('')

#二行数量
for topping_value in recent_topping_allwance:
    print(topping_value,end='')
    print('\t',end='')
print('\n')

#空便条
requested_toppings = []
print('主角：豆皀，你批萨要加料不咯？','贼有钱：有啥，全都给我加一份，大爷有钱！','...低头写下来\n',sep='\n')

#需求：加
demand = 1

#无脑每样加1份（后期实际场景化）
a = 0
if demand == 1:
    for add in recent_toppings:
        print('加1份'+add)
        recent_topping_allwance[a] = recent_topping_allwance[a]-1
        a = a + 1


#点完后余量记录
print()
print('\t**** 配料余量表（更新） ****')
#首行名称
for topping_name in recent_toppings:
    print(topping_name,end='')
    print('\t',end='')
print('')

#二行数量
for topping_value in recent_topping_allwance:
    print(topping_value,end='')
    print('\t',end='')
print('\n')
