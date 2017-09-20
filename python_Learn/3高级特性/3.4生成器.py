

# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：
# generator。


print('第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：')

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
print('调用方法')
print(next(g))
for n in g:
    print(n)