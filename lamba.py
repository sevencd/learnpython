square = lambda x: x ** 2
print(square(3))

print([(lambda x: x * x)(x) for x in range(10)])

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])
print(l)

"""
from	tkinter	import	Button,	mainloop
button	=	Button(
            text='This	is	a	button',
            command=lambda:	print('being	pressed'))	#	点击时调⽤lambda函数
button.pack()
mainloop()
"""
# 函数式编程
squared = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l)  # [2,	4]
print(new_list)
lreduce = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, lreduce)  # 1*2*3*4*5	=	120
# print(product)
