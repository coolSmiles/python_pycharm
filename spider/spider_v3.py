"""
cookie模块
"""
from urllib import request
from http import cookiejar

# 创建一个cookieJar实例,用来保存cookie对象(cookie对象保存在内存中的)
# cookie = cookiejar.CookieJar()

# 将cookie保存在文件中
fileName = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar()

# 创建一个HTTPCookieProcessor来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建一个opener
opener = request.build_opener(handler)

resp = opener.open("https://aa-uat.zhongan.com")

cookie.save(fileName, ignore_discard=True, ignore_expires=True)

