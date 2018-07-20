"""
使用proxyHandler 设置代理服务器
"""

from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baidu.com"

    #设置代理服务器地址
    proxys = {
        'http':'47.100.226.224:3128'
    }

    #创建proxyHandler
    proxy_handler = request.ProxyHandler(proxies=proxys)

    #创建opener
    opener = request.build_opener(proxy_handler)

    #安装opener 后面所有使用urlopen()的地方都会使用安装的opener
    request.install_opener(opener)

    try:
        resp = request.urlopen(url=url)

        html = resp.read().decode()

        print(html)
    except Exception as e:
        print(e)

    else:
        print('.....done.....')
