def make_pizza(size, *toppings):
    """ 概述要制作的比萨 """
    print("\n做一个 " + str(size) +
    "-寸批萨，要包含以下食材:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese','green peppers')

import global_variable
print(global_variable.gl_name)
