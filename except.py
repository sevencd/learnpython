"""
try:
    s = input('please	enter	two	numbers	separated	by	comma:	')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
except    ValueError    as    err:
    print('Value	Error:	{}'.format(err))
except    Exception    as    err:
    print('Other	error:	{}'.format(err))
finally:
    print('不管什么异常都执行')

print('continue')
"""


class MyInputError(Exception):
    """Exception	raised	when	there're	errors	in	input"""

    def __init__(self, value):  # ⾃定义异常类型的初始化
        self.value = value

    def __str__(self):  # ⾃定义异常类型的string表达形式
        return "{}	is	invalid	input".format(repr(self.value))


try:
    raise MyInputError("dfds参数")  # 抛出MyInputError这个异常
except    MyInputError    as    err:
    print('error:	{}'.format(err))

d = {'name': 'jason', 'age': 20}
value = ' d'
if 'dob' in d:
    value = d['dob']
print(value)
