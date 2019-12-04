def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1


"""
yield对于初学者来说，你可以理解为，函数运行到这一行的时候，程序会从这里 暂停，然后跳出，
不过跳到哪里呢？答案是 next() 函数。那么 i ** k 是干什么的呢？它其实成了 next() 函数的返回值。
 这样，每次 next(gen) 函数被调用的时候，暂停的程序就又复活了，从 yield 这里向下继续执行；
"""

gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)


get_sum(8)


def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))

"""
def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
"""


def is_subsequence(a, b):
    b = iter(b)
    print(b)
    gen = (i for i in a)
    print(gen)
    for i in gen:
        print(i)
    gen = ((i in b) for i in a)
    print(gen)
    for i in gen:
        print(i)
    return all(((i in b) for i in a))


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
