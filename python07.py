#将一个列表的数据复制到另一个列表
a = [1,2,3]
b = a[:]
c = a.copy()#copy.copy(a)
print(b)
print(c)

#len,append
lst = [1,2,3]
v = []
for i in range(len(lst)):
    v.append(lst[i])
print(v)

#for in
x = [j for j in lst]
print(x)