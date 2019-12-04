# 装饰器
import functools
"""
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


# greet = my_decorator(greet)
@my_decorator
def greet():
    print('hello world')


greet()
"""

# 带有参数的装饰器
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')
"""


# 带带有有自自定定义义参参数数的的装装饰饰器


def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


greet('hello world')
print(greet.__name__)
print(help(greet))
# 装饰器嵌套
