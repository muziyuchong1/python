#题目 :输入某年某月某日,判断这一天是这一年的第几天
#分析 :以3月5日为例,应该先把前两个月的加起来,再加上5天即本面的第几天,
#     特殊情况,闰年且输入月份大于2时需考虑加一天

###############################
#判断是否是闰年
def method():
    year = (input('your Year:'))
    if not year:
        year = None
    else:
        year = int(year)
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
            print("the year {} is {}".format(year,"闰年"))
        else:
            print("the year {} is {}".format(year,"平年"))

def main():
    while True:
        year = input('your Year:').strip()
        if not isinstance (year,int):
            method()
        else:
            raise ("您输入的年份类型有误")

main()


#########################################
#判断这一天是这一年的第几天

def fn():
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    #每个月的天数
    nonleapyear = [31,28,31,30,31,30,31,31,30,31,30,31] #平年
    #leapyear = [31,29,31,30,31,30,31,31,30,31,30,31] #闰年
    #可以得到逻辑:闰年且输入月份大于2时需考虑加一天
    if 0 < month <= 12:
        num = day
        for i in range(0,month-1):
            num+=nonleapyear[i]

        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            if month>2:
                num = num+1
                print("你输入的日期是这一年的第{}天".format(num))
            else:
                print("你输入的日期是这一年的第{}天".format(num))
        else:
            print("你输入的日期是这一年的第{}天".format(num))
    else:
        print("ERROR of Month")

fn()


#####################
import time
D = input('date:')
dayth = time.strptime(D,'%Y-%m-%d').tm_yday
print("第 {} 天 ".format(dayth))

