"""
name = input('your	name:')
gender = input('you	are	a	boy?(y/n)')
print(name)
print(gender)
welcome_str = 'Welcome	to	the	matrix	{prefix}	{name}.'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}
print('authorizing...')
print(welcome_str.format(**welcome_dic))
a = input()
b = input()
print('a	+	b	=	{}'.format(a + b))
print('type	of	a	is	{},	type	of	b	is	{}'.format(type(a), type(b)))
print('a	+	b	=	{}'.format(int(a) + int(b)))
"""
import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}
with open('params.json', 'w')    as    fout:
    params_str = json.dump(params, fout)
with    open('params.json', 'r')    as    fin:
    original_params = json.load(fin)
print('after	json	deserialization')
print('type	of	original_params	=	{},	original_params	=	{}'.format(type(original_params),
                                                                                       original_params))
