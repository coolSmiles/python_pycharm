from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # url = 'http://c-uat.zhongan.com'

    resp = requests.get(url)

    headers = resp.headers  # 响应头信息
    encoding = resp.encoding  # 响应的encoding
    resp_content = resp.content  # content 内容为bytes类型
    resp_text = resp.text  # text ，Requests会自动解密服务器的内容
    resp_json = resp.json  # json Requests 内置json模块，把结果转成json

    utils_headers_encoding = requests.utils.get_encoding_from_headers(headers)
    utils_content_encoding = requests.utils.get_encodings_from_content(str(resp_content))
    print(utils_headers_encoding)
    print(utils_content_encoding)
    print(resp.encoding)

    resp.encoding = utils_content_encoding

    print(resp.text)

    soup = BeautifulSoup(resp.text, 'lxml')

    print(soup.title.text)
