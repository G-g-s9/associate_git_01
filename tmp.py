'''tmp'''

x_sum = 0
i = 1
flag = 0
while i<20:
    x_sum = x_sum + (-1)**flag*(1/2**i+1/3**i)
    flag+=1
    i+=2
        
print(4*x_sum)
print(i)
print(flag)
print(1/3**2*9)
