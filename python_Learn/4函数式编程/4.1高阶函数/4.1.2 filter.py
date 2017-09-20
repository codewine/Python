



#
# Python内建的filter()函数用于过滤序列。
#
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。


def is_odd(n):
    return n % 2 == 1

lf = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(lf)


def not_empty(s):
    return s and s.strip()

f = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(f)

# 用filter求素数
# 生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#筛选
def _not_divisible(n):
     return lambda x: x % n > 0

# 生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break