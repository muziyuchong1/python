#对象是带有附加方法的数据，闭包是带有数据的函数（）方法
def make_counter():
    i = 0
    def counter():# counter is a closure
        nonlocal i
        i+=1
        return i
    return counter
a = make_counter()
b = make_counter()
print( a(),a(), b(),b())

#闭包允许您将变量绑定到函数,而不将它们作为参数传递

