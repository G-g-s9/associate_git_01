import random
print('\t\n#*  人生的不同阶段\n')
print('\t\n随机数（1-110）直接判断（后期考虑交互录入）\n')

sb_age = int(random.random()*110)
print('年龄：'+str(sb_age))

if sb_age < 2:
    print('你是巨婴？！')
elif sb_age < 4:
    print('你现在能走了不？走路利索不？小阔爱🦐')
elif sb_age < 13:
    print('儿童，木木屋童鞋要了解下布🙈')
elif sb_age < 20:
    print('青年，小伙子呦～')
elif sb_age < 65:
    print('成年人。你要像个大人的亚子')
elif sb_age < 80:
    print('养老金，可要记得领取呦～')
elif sb_age < 110:
    print('恭喜您，依然建在')
    
