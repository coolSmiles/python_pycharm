'''
1、求输入数的平方根 input() 输入默认接收到的类型是字符串str
'''

#第一种求平方根的方法（只可以求正数的）
m = float(23)
n = m ** 0.5

print('%0.2f 的平方根为 %0.2f'%(m ,n))

#第二种求平方根的方法(可以求实数和复数的)
import cmath

m = 2 + 3j
n_sqrt = cmath.sqrt(m)

print(' {0} 的平方根 实部为 {1: 0.3f} ,虚部为 {2:0.3f}'.format(m,n_sqrt.real,n_sqrt.imag))

'''
2、二次方程式 ax**2 + bx + c = 0
   a、b、c 用户提供，为实数，a ≠ 0
'''
a,b,c = 1,2,-3

d = ( b ** 2 / a ** 2 ) * 1/4 - c/a
if d < 0:
    raise Exception('输入的参数不合法')
f = cmath.sqrt(d)

print('二次方程式 ax**2 + bx + c = 0 的解为：',f - b/2*a)

'''
3、用户输入三角形三边长度，并计算三角形的面积:底面积乘以高除以2
'''

'''
4、生成 0 ~ 9 之间的随机数
'''
import random
print('0~9中的一个随机数：',random.randint(0,9))

'''
5、判断字符串是否为数字
number有三种类型：int、float、complex
也可以用str.isdigit()来判断
'''

def is_number(a):

    try:
        float(a)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(a)
        return True
    except ValueError:
        pass

        return False

print("is_number(1)",is_number(1))
print("is_number(四)",is_number('四'))
print("is_number(@)",is_number('@'))

print("isdigit(123)",'123'.isdigit())
print("isdigit(1abc)",'1abc'.isdigit())

'''
6、将字符串转换为大写字母，或者将字符串转为小写字母
'''
print('werBB'.lower())
print('werbb'.upper())
print('werbb'.count('b'))
print('www.baidu.com'.title())
print('www.baidu.com'.capitalize())







