import copy

l1 = [1, 2, 3]
l2 = list(l1)
print(l1)
print(l2)
print(l1 == l2)
a = 2570
b = 2570
print(a == b)
print(a is b)
print(id(a))
print(id(b))

t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
t1[-1].append(5)
print(t1 == t2)
print(t1 is t2)
t3 = (1, 2)
t4 = (1, 2)
print(t3 == t4)
print(t3 is t4)
# 浅拷贝
"""
l1 = [[1, 2], (30, 40)]
l2 = list(l1)
l1.append(100)
l1[0].append(3)
print(l1)
print(l2)
l1[1] += (50, 60)
print(l1)
print(l2)
"""

# 深拷贝
"""
l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)
l1.append(100)
l1[0].append(3)
print(l1)
print(l2)
"""
x = [1]
x.append(x)
print(x)
y = copy.deepcopy(x)
print(y)
