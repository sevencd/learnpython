s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)
s = 'a\nb\tc'
print(s)
print(len(s))
name = 'jason'
for char in name:
    print(char)
s = ''
for n in range(0, 100):
    s += str(n)
print(s)
l = []
for n in range(0, 100):
    l.append(str(n))
l = ' '.join(l)
print(l)
path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0]  # 返回'ads'
table = path.split('//')[1].split('/')[1]  # 返回	'training_table'
print(namespace)
print(table)
print('no data available for person with id: {}, name: {}'.format(2, name))
