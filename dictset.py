s = {1, 2, 3}
print(1 in s)
d = {'name': 'jason', 'age': 20}
print(d['name'])

d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
# d1 == d2 == d3 == d4
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
s1 == s2
# True
