"""
def find_largest_element(l):
    if not isinstance(l, list):
        print('input	is	not	type	of	list')
        return
    if len(l) == 0:
        print('empty	input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest	element	is:	{}'.format(largest_element))


find_largest_element([8, 1, -3, 2, 0])
"""

"""
def my_sub_func(message):
    print('Got	a	message:	{}'.format(message))


def my_func(message):
    my_sub_func(message)  # 调⽤my_sub_func()在其声明之前不影响程序执⾏


my_func('hello	world')
"""


def sum1(a, b):
    return a + b


print(sum1(1, 2))
print(sum1([1, 2], [3, 4]))
print(sum1('hello	', 'world'))

# 函数嵌套

"""
def factorial(input):
    # validation	check
    if not isinstance(input, int):
        raise Exception('input	must	be	an	integer.')

    if input < 0:
        raise Exception('input	must	be	greater	or	equal	to	0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input - 1)

    return inner_factorial(input)


print(factorial(5))
"""

# 函数的作用域
"""
MIN_VALUE = 1
MAX_VALUE = 10


def validation_check(value):
    MIN_VALUE = 3
    MIN_VALUE += 1
    print(MIN_VALUE)
    # global MIN_VALUE
    # MIN_VALUE += 1


validation_check(5)
print(MIN_VALUE)
"""


# 闭包

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是exponent_of函数


square = nth_power(2)  # 计算⼀个数的平⽅
cube = nth_power(3)  # 计算⼀个数的⽴⽅
print(square(2))		#	计算2的平⽅
print(cube(2))	#	计算2的⽴⽅