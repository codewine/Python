def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(5))

# print(fact(1000))

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式
# 尾递归调用时，如果做了优化，栈不会增长，
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')