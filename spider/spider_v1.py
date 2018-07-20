from urllib import request, parse
import json

'''
爬取一个请求的内容，并获取我们需要的内容
'''
if __name__ == '__main__':
    url = 'http://c.itest1.zhongan.com/vehicle/affiche/affiche_controller/query_affiche_list.json'

    data = {
        'keyWord': '12',
        'pageNo': 1,
        'pageSize': 20,
        'afficheStatus': '1'
    }

    # 使用post请求，data类型必须是bytes类型
    data = parse.urlencode(data).encode()

    print(type(data))

    assert isinstance(data, object)

    resp = request.urlopen(url, data)

    html = resp.read().decode()

    print(html)

    print(type(html))

    assert isinstance(html, object)
    result_dict = json.loads(html)
    print(type(result_dict))

    if result_dict['success']:
        value_dict = result_dict['value']
        for item in value_dict['rows']:
            print("公告id：{0},公告内容：{1}".format(item['afficheId'], item['content']))
    else:
        print('faile')

