listtuper = []
print(listtuper.__sizeof__())

listtuper.append(1)
print(listtuper.__sizeof__())
listtuper.append(2)
print(listtuper.__sizeof__())

b = (i for i in range(5))
print(2 in b)
print(4 in b)
print(3 in b)
