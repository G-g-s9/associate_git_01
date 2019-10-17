### 定义函数.本例二次函数

def quadratic_function(x,a = 1,b = 1,c = 0):
    """给定系数的二次函数求值"""
    y_qf =a * x ** 2 + b * x + c
    message_c = "+"+str(c)
    if c==0:
        message_c=""
    message_b = "+"+str(b)+"*"+"x"
    if b==0:
        message_b = ""
    elif b==1:
        message_b = "+"+"x"
    message_a = str(a)+"*"+"x^2"
    if a==0:
        message_a = ""
    elif a==1:
        message_a = "x^2"

    message = "当 x = "+str(x)+"时，\n"+"函数 y= "+message_a + \
    message_b + message_c+"\ny值为 "+str(y_qf)
    return message
print(quadratic_function(4,1,3))
