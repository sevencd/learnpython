'''
id = input("input id:")
if id == 0:
    print('red')
elif id == 1:
    print('yellow')
else:
    print('green')
'''
text = '	Today,		is,	Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
print(text_list)
