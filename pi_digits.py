

# ~ π/4≈（1/2+1/3）-1/3*（1/2**3+1/3**3）+1/5（1/2**5+1/3**5）-......
print("用公式求π\n\
π/4 ≈（1/2+1/3）-1/3*（1/2**3+1/3**3）+1/5（1/2**5+1/3**5）-...\n\n")
        


def pi():
    '''计算相对精度的π值'''
    accuracy = 2*int(input("要 求到哪种程度（默认4项精度就够了）\n请输入项数："))
    x_sum = 0
    i = 1
    flag = 0
    while i<accuracy:
        x_sum = x_sum + (-1)**flag*1/i*(1/2**i+1/3**i)
        flag+=1
        i+=2
        
    return x_sum*4
y = pi()

g = '%.'+str(70)+'f'
print(g%y)


from decimal import *
getcontext().prec = 53      # 显示小数点后53位，实际python就52位相当于双double

x_sum = 0
i = 1
flag = 0
x_sum = x_sum + (-1)**flag*1/i*(1/2**i+1/3**i)
print(Decimal(x_sum))
print("小数点后"+str(len(str(Decimal(x_sum)))-2)+"位")
