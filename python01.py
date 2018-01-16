#题目   有四个数字:1,2,3,4,能组成多少个互不相同且无重复的三位数?各是多少?
#分析   三位数,各位十位百位数字都是在(1,2,3,4)中,循环三次,组成的数中去点不满足条件的
##################################################
#for循环
num = 0
# a = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            # if i!=j and i!=k and j!=k:#各位十位百位没有重复的数字
            num +=1
            print(i,j,k)
            # a.append([i,j,k])
print(num)

##################################################
#用数量统计和累加
from itertools import permutations
t = 0
for  i in permutations('1234',3):
    print(''.join(i))
    t += 1
print("数量是:%s"%t)