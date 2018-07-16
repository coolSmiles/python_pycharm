print("hello")
# 注释
#if elif else 逻辑判断
string = 1;
if string > 0 :
    print("大于0")
elif string < 0 :
    print("小于0")
else :
    print("等于0")

#import
import sys
for i in sys.argv:
    print(i)
print ('\n python 路径为',sys.path)
#Number 类型
a,b,c = 1,1.2,1+2j;
print(type(a),type(b),type(c))
print(isinstance(a,int))
#String 类型 \ 反斜杠表示转义，签名加个r表示不转义；Python中字符串不能修改
print("fi\nal")
print(r"fi\nal")
#list 列表，列表写在[]中，数据类型可以不一样，同时支持截取和索引,同时列表中元素是可以改变的,可以进行拼接
lists = [1,'hello',2]
print(lists)
print(lists[0])
print(lists[0:3])
lists[2] = 3
print(lists[0:3])
'''
#Tuple 使用（） 元组和列表类似，不同的是，元组不能修改
当元组中只有一个元素时，需要加逗号，否则括号会被当成运算符使用
'''
tuple = ('hello','world',1)
tuple_2 = (2,'world','hello')

tuple_3 = (3)
print(type(tuple_3))
tuple_4 = (4,)
print(type(tuple_4))



print(tuple + tuple_2)
print(tuple_2 * 2)

#Set集合：是一个无序不重复的序列，可以使用{} 大括号或者set()方法创建，如果要创建一个空集合，只能用set();
#Set集合可以进行集合运算，
student = {'张三','李四','王五'}
print(student)

if ('张三' in student) :
    print("张三是学生")
else :
    print("张三不是学生")

a = set('abcedf')
b = set('abcd')
print(a - b)
student.add('赵六')
student.remove('赵六')
print(student)

'''
#Dictionary 字典:是一种内置的数据类型，list是有序的对象集合，字典是无序的对象集合，字典是一种映射关系，可以通过键值获取vlaue
#类型java中的Map ,字典用{}大括号表示，它是一个无序的键值对集合 'key':'value'
'''

dict = {'key1':'value1','key2':'value2','key3':'value3'}
print(dict['key1'])
print(dict.keys())
print(dict.values())
print(dict.get('key1'))

"""
#数据类型转换
"""
print(float(23))
print(int(23.2))


'''
python 运算符：逻辑运算符 
    Python  java
与    and     &&
或    or      ||
非     not    !
'''
a,b = 1,2
if (a > 1 or b > 1):
    print("1")
elif (a > 1 and b < 1):
    print("2")
else :
    print("3")

'''
成员运算符： in  not in
'''

if (a in lists) :
    print("1 in list")
else :
    print("1 not in list")

'''
身份运算符：is ：判断对象是否相等，is not 判断对象是否不相等。
x is y 类似 id(x) == id(y)
id():用户获取对象内存地址

is 与 == 的区别：is 用于判断对象是否相等，== 判断变量的值是否相等
'''
a = 1
b = 1
print('a对象的内存地址：' + str(id(a)))
print('b对象的内存地址: ' + str(id(b)))
if (a is b ):
    print("a 和 b 是同一个对象")
elif (a == b):
    print("a 和 b 的值相等")
else:
    print("..")

if (a == b):
    print("a 和 b 的值相等")
else:
    print("a 和 b 不相等")

'''
数学函数:python 的数据类型是不允许改变的 
所以：字符串 + 数字 不等于 字符串，需要把数字转成字符串才可以做拼接操作
'''
print('绝对值' + str(abs(-10)))

import math #导入math模块
print('上入整数' + str(math.ceil(4.1)))
print('下舍整数' + str(math.floor(4.9)))
print('四舍五入' + str(round(2.343,2)))
print('对数' + str(math.log(100,10)))
print('10为基数的对数' + str(math.log10(2)))
print('返回最大值' + str(max(1,2)))
print('返回最小值' + str(min(1,2)))
print('指数运算后的值' + str(pow(2,3)))

'''
随机函数 
'''
import random
#从序列的元素中随机挑选一个元素
print(random.choice(range(10)))
print(range(10))
#从指定递增基数集合中获取一个随机数
#randrange(start,end,step)  step 默认是1
#从1-100 随机选择一个奇数
print(random.randrange(1,100,2))
#从0——99 返回一个随机数
print(random.randrange(100))

#random()随机生成一个实数，范围在[0,1）范围内
print('随机生成一个实数：' + str(random.random()))

'''
三角函数
'''
print("正弦：" + str(math.sin(math.pi/2)))
print("余弦：" + str(math.cos(math.pi)))
print("正切：" + str(math.tan(math.pi/2)))
print('将角度装成弧度' + str(math.radians(180)))

'''
python  格式字符串 
%s 格式化字符串
%d 格式化整数
'''
print('我是 %s ，今年 %d 岁！' %('小米',20))

'''
python 三引号 """ :允许一个字符串跨多行，字符串可以包含，换行符，以及其他特殊字符。
'''
param_str = """
    这是一个三引号的开始
    
    TAB(\t)
    
    这是一个三引号的结束

"""
print(param_str)

print(len(lists))
print(lists + [3,'wold'])
print(lists)

'''
字典操作
'''
#访问字典中的值,如果用字典中没有的键访问数据，会报错
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict['Name'])
#print(dict['name'])
#修改字典值
dict['Name'] = 'bobo'
print(dict['Name'])
#删除字典中的值
del dict['Name']
dict.clear() #清空字典里面的值
del dict #删除字典
'''
字典的特性：
1、不允许key出现两次，后面的一个值会被会覆盖前一个值  类似java中的map
2、键必须不可变。
'''
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

#随机删除键值对，一般删除末尾对
dict.popitem()
print(dict)

'''
集合操作:集合是一个包含不重复元素的一个列表
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket.add('jianguo')
print(basket)
#remove :移除元素，如果元素不存在会报错
basket.remove('jianguo')
#discard 也可以做移除元素操作，元素不存在，也不会报错
basket.discard('aa')
#pop随机删除一个元素
basket.pop()
print(basket)

'''
for 语句
'''
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    if x == 'C++':
        continue
    print(x)

'''
range():可以生成数列，如果要遍历数字数列,同时也可以指定不同的增量

1、可以结合 len() 函数以遍历一个序列的索引
2、还可以使用range()生成一个列表
'''
for i in range(0,3):
    print(i)

for i in range(0,10,3):
    print(i)

for x in range(len(languages)):
    print(languages[x])
print(lists)

arrylist = list(range(5))

print(arrylist)

'''
迭代器与生成器
迭代器：可以记住遍历位置的一个对象

iter()，可以将字符串，list、元组装换成一个迭代器对象
'''
#创建一个迭代器对象
it = iter(languages)
for i in it:
    print(i ,end=',')

my_name = 'zhangsan'
for my in iter(my_name):
    print(my ,end=',')

lan = languages.__iter__()
for l in lan:
    print(next(lan))


'''
生成器：在python中使用了yield的函数被称为生成器
和普通函数不一样的是，生成器是一个返回迭代器的函数，只能用于迭代操作，简单点理解就是生成器就是一个迭代器
一种直观的解释是：程序执行到yield的时候，会暂停返回值并暂停，直到再次调用next()的方法的时候，程序才会在
之前暂停的地方继续开始执行。
'''
import traceback
def my_generator(n): #定义一个生成器函数
    a = 0
    while True:
        if(a > n):
            return
        yield a
        a += 1

f = my_generator(5) #生成一个迭代器函数，用于迭代操作

'''
while True:
        try:
            print(next(f), end=',')
        except StopIteration:
            #sys.exit()
            traceback.print_exc()
'''
'''
Python函数
定义：
def 函数名(参数列表)：
    函数体
'''
'''
函数的参数传递：类型是属于对象，变量没有具体类型。

不可变类型：string,tuple,number 
可变类型：list 字典，集合等。

python 可以接收这两种参数类型

函数参数类型：
必须参数
关键字参数
默认参数
不定长参数
'''

#必须参数
def must_args( age ):
    print(age)


#must_args()

#关键字参数:使用关键字参数允许函数调用时的参数与函数定义的参数顺序不一致，因为Python解析器
#可以用参数名匹配参数
def keyword(str1):
    print(str1)
    return
keyword(str1='hello world')

def student_def(name,age):
    print("name="+name+",age="+age)

student_def(age='24',name='zhangsan')

#默认参数：如果函数调用时没有传递参数，则使用默认参数
def default_def(name,age=23):
    print("name",name)
    print("age",age)

default_def(name='lisi')

#不定长参数：当函数调用时，可能需要传入比之前定义的参数更多，所以就需要把函数定义为不定长函数
'''
    加了 * 的参数，将以元组的形式传入
    加了 ** 的参数，将以字典的形式传入
    如果 * 单独存在，那么* 后面的参数必须以关键字传入
    
    定义的参数可以多传，但是不可以少传
'''

def function_one(a,*b):
    print(a)
    print(b)

function_one(1)
function_one(2,'hello','world')

def function_two(a,**b):
    print(a)
    print(b)

function_two(2,c=1,d=3)

def function_three(a,*,b):
    print(b)

function_three(1,b=10)


'''
匿名函数：
Python使用lambda来创建匿名函数
'''

function_sum = lambda a , b: a + b

print("a+b的值：",function_sum(1,2))

'''
变量的作用域：
B:内建作用域
G:全局作用域
E:闭包函数外的函数中
L:局部作用域

查找规则：L>E>G>B
python中只有module、class、def/lamdba中才会引入新的作用域
'''

total = 0 #全局变量
def args_sum(a,b):
    c = 1 # #局部变量
    total = a + b #total函数中的局部变量
    print(total)
    def total_args(d):
        e = 0#局部变量

args_sum(1,1)
print("全局变量total:",total)

'''
如果要在函数中使用全局和局部变量需要用到globle和nonlocal关键字
'''
sum = 0;
def args_sum_global(a,b):
    d = 1
    global sum
    sum = sum + a + b
    def args_sum_nonlocal():
        nonlocal d
        e = d
        print("nonlocal测试：",e)
    args_sum_nonlocal()
args_sum_global(1,2)
print("global args sum:",sum)


'''
数据结构：列表
列表的元素可以修改，字符串、元组的元素是不允许修改的

list：常用方法
'''

a = [66.25, 333, 333, 1, 1234.5]
print('列表中元素出现的次数 ：',a.count(333))
a.reverse()
print('倒排列表中的元素：',a)
a.sort()
print('对列表中的元素进行排序：',a)

'''
使用列表list，可以实现堆栈功能（先进后出）
'''
stack = [3, 4, 5]
#往栈顶压入一个元素
stack.append(6)
#从栈顶释放一个元素
stack.pop()
print(stack)

'''
把列表当做队列（先进先出），但是拿列表当做队列使用效率不高
因为在列表的最后添加或者弹出元素最快，然而在列表里面插入或者从头部弹出确不快，
因为所有的其他元素都要一个个移动
'''
import collections
deque_list = collections.deque(stack)
deque_list.appendleft(2)
print('popleft():',deque_list.popleft())
print(deque_list)

print("range():",range(5))
print(random.randrange(5))
print(type(range(3)))

'''
列表推导式
'''
vec = [2, 4, 6]
print([2*x for x in vec])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in freshfruit])

'''
嵌套列表
matrix 相当于一个3X4的矩阵
'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

#可以将它转成一个4X3的矩阵

print([ [row[i] for row in matrix]  for i in range(4)])

'''
字典：可以使用构造方法dict()来构建字典。
'''

print({2: 4, 4: 16, 6: 36})

'''
遍历技巧：字典遍历 items()
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
'''
列表遍历 enumerate()
'''
for i,v in enumerate(['hello','world']):
    print(i,v)

'''
同时遍历多个列表 zip()
'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q,a in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
fromat():用于格式化字符串
"""
print('{名字}今天{动作}'.format(名字='陈某某',动作='拍视频'))#通过关键字
grade = {'name':'zhangsna','age':33}
print('{name} this year age is {age}'.format(**grade)) #可用字典关键字传入，在字典前加上**
print('{0} this year age is {1}'.format('lisi','23')) #通过位置

'''
反向遍历一个列表：reversed()
'''
for i in reversed(range(4)):
    print(i)

'''
模块：import 
导入模块：
import moduel_name 导入整个模块 
from moduel_name import fib1,fib2 导入模块的fib1,fib2部分
from moduel_name import * 导入模块的所有（变量、函数）名称，有可能会覆盖掉原文件的变量、函数
'''

'''
__name__(双划线)属性
一个模块被一个程序第一次引入时，其主程序会运行，如果我们想在模块引入时莫模块不执行，
只有在模块自身在允许是才执行，可以使用__name__属性
每个模块都有一个__name__属性，当值为__main__时，表明该模块自身在运行，否则是被引入
'''

#import using_name

'''
dir() 内置函数，可以找到模块内定义的所有名称
如果没有给定参数，那么dir()函数会罗列出当前模块定义的所有名称
'''
#print(dir(using_name))

print(dir())

'''
读取键盘的输入input()
'''
#print('你输入的内容是：',input('请输入：'))


'''
文件的读和写 open(filename,'操作类型 mode')

mode:
a+:打开一个文件用于读写，指针位于文件末尾，文件打开时以追加的模式
'''

file = open('using_name.py','a+')

#file.write("print('hello,world')")

file.close()


'''
错误和异常

try except 还有一个可选的else字句放在所有except子句之后，在没有发生任何异常的情况下会执行。

finally

使用raise抛出一个指定的异常
'''

try:
    print('my age is ' ,23)

except:
    print('error message :',sys.exc_info()[0])
    raise
else:
    print('没有发生异常')

finally:
    print('finally 无论是否发生异常，都会执行')

'''
自定义异常类：异常类继承Exception
'''
class myExcetpion(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise myExcetpion(3)
except myExcetpion as e:
    print('occurred exception:',e.value)

'''
with 预定义的清理行为，例如当系统使用open打开一个文件的时候，文件会保持打开状态，
并且不会关闭，使用with关键字可以保证对象在使用完成之后，一定会执行他的清理方法
'''


'''
面向对象：类
类的方法和普通方法只有一个区别：类方法必须有一个额外的第一参数名称self
'''

class Test:
    def __init__(self):
        print('类的构造方法')

t = Test()

'''
继承，类继承的定义方式 className(BaseClassName) BaseClassName代表着基类

单继承：className(BaseClassName)
多继承：className(BaseClassName1，BaseClassName2,BaseClassName3....)
'''
class people:
    name = ''
    age = 0
    _sex = '' #protected变量，只有当前类和子类可以访问
    __hight = '' #private 私有变量

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def _getSex(self):#protected变量，只有当前类和子类可以访问
        return self._sex

    def __getHight(self):
        return self.__hight#private 私有方法

    def print_age_name(self):
        print('name:',self.name)
        print('age:',self.age)

p = people('zhangsan',23)
p.print_age_name()

class speaker:
    topic = ''#话题

    def __init__(self,topic):
        self.topic = topic

    def speaker(self):
        print('学生演讲的话题是',self.topic)

#单继承
class student(people):
    grades = ''#年级

    def __init__(self,name,age,grades):
        people.__init__(self,name,age)
        self.grades = grades

    def print_info(self):
        print('学生信息：{}，年龄{}岁，读{}'.format(self.name,self.age,self.grades))

stud = student('李四',24,'四年级')
stud.print_info()

#多继承

class HightStudent(people,speaker):

    def __init__(self,name,age,topic):
        people.__init__(self,name,age)
        speaker.__init__(self,topic)

'''
    def speaker(self): #方法的重写
        print('学生信息：{}，年龄{}岁,今天演讲的主题是{}'
              .format(self.name, self.age,self.topic)
'''

hs = HightStudent('王五',25,'Python基础入门')
hs.speaker()
super(HightStudent,hs).speaker()

import os
print('os.name',os.name)
print('os.paht',os.path)




