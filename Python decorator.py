#装饰器基础
#1 python的功能是对象
#############################################
def shout(word='yes'):
    return word.capitalize()+"!" #大写的
print(shout())

'''
作为一个对象，你可以将这个函数(t)赋值给一个变量，就像其他对象一样
'''
scream = shout

''' 注意，我们不使用圆括号:我们没有调用函数
    我们把这个函数的声音输入到变量"尖叫"中(scream)
    这意味着你可以从“尖叫”scream中喊出“大喊”shout:
'''
print(scream())


del shout
try:
    print(shout())
except NameError as e:
    print(e)

print(scream())


######################################################3
'''
Python 函数的另一个有趣的特性是它们可以在另一个函数中定义!
'''
def talk():
    '''You can define a function on the fly in "talk"
    你可以在talk中定义一个函数
    '''

    def whisper(word='yes'):
        return word.lower()+"..."
    print(whisper())

'''你称之为“谈话”talk，它定义了“耳语”whisper，每次你调用talk，
然后在talk中又会调用whisper
'''
talk()

'''但是“whisper”并不存在于“talk”之外:'''

try:
    print(whisper())
except NameError as e:
    print(e)



#2 函数引用
#######################################################
'''好的继续,上面我们可以看到函数是对象,它的功能:
    可以分配给一个变量
    可以在另一个函数中定义
    这意味着函数可以返回另一个函数
'''
def gettalk(kind="shout"):

    '''We define functions on the fly动态定义函数'''
    def shout(word='yes'):
        return word.capitalize()+'!!!'
    def whisper(word='yes'):
        return word.capitalize()+'...'

    '''Then we return one of them返回其中的一个'''

    if kind =='shout':
        '''We don't use "()", we are not calling the function,
           不使用(),没有调用函数
            返回函数对象
        '''
        return shout
    else:
        return whisper

'''如何用这样的函数'''
'''获取函数并将其赋值给变量'''

talk = gettalk()
'''talk在这里是一个函数对象,这个对象就是函数返回的一个函数'''
print(talk)
print(talk())

'''你甚至可以直接使用她'''
print(gettalk('whisper')())


#3手工装饰
##############################################
'''装饰器是一个函数，它期望另一个函数作为参数'''

def my_shiny_new_decorator(a_function_to_decorate):
    '''在内部，装饰器在动态定义一个函数:包装器,wrapper
        这个包装器函数将被包裹在原始的函数中
        可以在它之前或者之后执行代码
    '''
    def the_wrapper_around_the_original_function():
        '''把你想要在原始函数被调用之前执行的代码放在这里'''
        print('Before the function runs')

        '''在这里调用函数(使用括号)'''
        a_function_to_decorate()

        '''在这里输入你想要在原始函数被调用后执行的代码'''
        print('After the function runs')

        '''我们返回刚刚创建的包装器函数'''
    return the_wrapper_around_the_original_function()


'''现在假设你创建了一个你不想再接触的函数'''
def a_stand_alone_function():
    print("I am a stand alone function,don't you dare modify me")
a_stand_alone_function()

'''你可以装饰它来扩展它的行为
将它传递给装饰器，它将动态地包装它
你想要的任何代码，然后返回一个新函数，准备使用'''
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
'''覆盖函数名'''
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
# '''以上就是装饰器的作用'''
print('------------------')

#4 语法糖
##################################################
@my_shiny_new_decorator
def new_stand_alone_function():
    print('leave me alone')
# new_stand_alone_function()


#5 练习装饰器代码(双层)
# ##################################################

def bread(func):
    def wrapper():
        print('</=====\>')
        func()
        print('<\=====/>')
    return wrapper

def ingredients(func):
    def wrapper():
        print('   MMM')
        func()
        print('   WWW')
    return wrapper


#积累调用
def async ():
    print('   ***')

async=(bread(ingredients(async))) #等价式,覆盖函数名
async()


#语法糖

@bread
@ingredients
def async ():
    print('ZZZZ')
async()

#6练习
###########################################
def makebold(fn):
    '''装饰器返回的新功能'''
    def wrapper():
        '''在前后插入一些代码'''
        return "<b>" + fn() +"</b>"
    return wrapper

def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() +"</i>"
    return wrapper
@makebold
@makeitalic
def say():
    return "hello"
print(say())

say =makebold(makeitalic(say))
print(say())


#7带参装饰器
#########################################################
#这不是黑魔法，你只需要让包装器wrapper传递参数:
def a_decorator_passing_arguments(function_to_decorator):
    def a_wrapper_accepting_arguments(arg1,arg2):
        print("this decorate have arguments look {} {}".format(arg1,arg2    ))
        function_to_decorator(arg1,arg2)
        print('ok')
    return a_wrapper_accepting_arguments
    '''因为当您调用装饰器返回的函数时，您将调用包装器，将参数传递给包装器将使其传递给包装器'''

@a_decorator_passing_arguments
def print_full_name(first_name,last_name):
    print("my name is {} {}".format(first_name,last_name))

print_full_name('jack','william')

#Python 的一个巧妙之处在是, 方法和功能是完全相同的。唯一的区别是,
# 方法期望其第一个参数是对当前对象 () 的引用。self
#这就意味着你可以用同样的方法构建一个技术的装饰。请记住考虑到:self
def method_friendly_decorate(method_to_dectorate):
    def wrapper(self,lie):
        lie = lie - 3
        return method_to_dectorate(self,lie)
    return wrapper

class A():
    def __init__(self):
        self.age = 32

    @method_friendly_decorate
    def sayYourAge(self,lie):
        print('i am {}'.format(self.age + lie))

l = A()
l.sayYourAge(-3)
###############################################################################
#通用的装饰--你将会应用于任何函数或方法, 不管它的参数是什么--然后只使用:*args, **kwargs
def a_decorator_passing_arbitrary_arguments(funvtion_to_decorate):
    '''包装器接受任意参数'''
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('have args?')
        print(args,kwargs,end=' ')

        '''然后你打开参数，这里是args，kwargs
            如果你不熟悉解包，请检查'''
        funvtion_to_decorate(*args,**kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print('Python is cool, no argument here.')
function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument(a,b,c):
    print(a,b,c)
function_with_no_argument(1,2,3,x='06')

@a_decorator_passing_arbitrary_arguments
def function_with_names_arguments(a,b,c,say='hello'):
    print('{},{} and{} speak say {}'.format(a,b,c,say))
function_with_names_arguments('jay','lee',say='good!')

class  B():
    def __init__(self):
        self.age = 31
    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self,lie=-3):
        print('I am {},ok?'.format(self.age+lie))
a = B()
a.sayYourAge()

#######################################################################
#装饰必须接受一个函数作为参数。因此, 不能将修饰函数的参数直接传递给修饰符。
#小提示
#修饰符只是普通函数
def my_decorator(func):
    print('我是初始的函数')
    def wrapper():
        print('然后增加了装饰功能')
        func()
    return wrapper
#你可以不带任何“@”来调用它
def lazy_function():
    print('zzzzz')
decorated_function = my_decorator(lazy_function)
decorated_function()

'''或者'''
@my_decorator
def lazy_function():
    print('zzzzz')


#让我们变得邪恶

def decorator_maker():
    print("  我创造装饰师!我只被执行一次,当你让我创建一个装饰师 ")
    def my_decorator(func):
        print("我是一个装饰!只有当你装饰一个函数时才会执行")
        def wrapper():
            print("我是装饰函数的包装器,\
                    当你调用装饰函数时,\
            作为包装器，我返回装饰函数的结果,增强的结果")
            return func() #返回初始函数的调用
        print("作为装饰器函数,返回包装器")
        return wrapper
    print('返回,生成装饰器函数')
    return my_decorator

#简便的方式
@decorator_maker()
def a():
    print("i am  the one")
a()


#8实例增加函数执行时长的功能
################################################################3
def benchmark(func):
    '''一个显示函数所花费时间的装饰器'''
    import time
    def wrapper(*args,**kwargs):
        print('1')
        t = time.clock()
        res = func(*args,**kwargs)
        print('1')
        print('{} {}'.format(func.__name__,time.clock()-t))
        return res
    return wrapper


def logging(func):
    '''一个记录脚本活动的装饰器'''
    def wrapper(*args,**kwargs):
        print('2')
        res = func(*args,**kwargs)
        print('2')
        print('{}{}{}'.format(func.__name__,args,kwargs))
        return res
    return wrapper


def counter(func):
    '''一个打印函数被执行的次数的装饰器'''
    def wrapper(*args,**kwargs):
        print(3)
        wrapper.count = wrapper.count + 1
        res = func(*args,**kwargs)
        print(3)
        print('{} has been uses:{}x'.format(func.__name__,wrapper.count))
        return res
    wrapper.count=0
    return wrapper

@benchmark
@logging
@counter
def reverse_string(string):
    return str(reversed(string))
print(reverse_string('WHAT'))

#装饰器的好处就是无需重写,直接调用

@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib.request import urlopen
    import urllib.request
    result = urllib.request.urlopen("https://weibo.com/u/2078648615/home?topnav=1&wvr=6")
    try:
        value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
        print('ok')
    except:
        print(result.info())

print(get_random_futurama_quote())



#9 python本身提供了几个装饰器,property,classmethod,staticmethod
#Django使用装饰器来管理缓存,查看权限
#异步函数调用


#10可以编写一个工厂函数, 它返回一个修饰符, 该功能在传递给工厂函数的标记中包装装饰函数的返回值
from functools import wraps

def wrap_in_tag(tag):
    def factory(func):
        @wraps(func)
        def decoratorj():
            return '<%(tag)s>%(rv)s</%(tag)s>' % (
                {'tag': tag, 'rv': func()})
        return decoratorj
    return factory
@wrap_in_tag('b')
@wrap_in_tag('i')     #语法糖等于是构造等价式,不要忘了构造
def say():            #say = wrap_in_tag('b')(wrap_in_tag('i')(say))
    return 'hello'
say()
