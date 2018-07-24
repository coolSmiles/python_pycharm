"""
lxml
"""

from lxml import etree
from bs4 import BeautifulSoup

if __name__ == '__main__':

    xml_string = '<root><foo id="foo-id" class="foo zoo">Foo</foo><bar>中文</bar><baz></baz></root>'

    root = etree.fromstring(xml_string)

    print(type(root))

    print(etree.tostring(root, pretty_print=True).decode('utf-8'))

    root_tree = root.getroottree()

    print(type(root_tree))

    tree_root = etree.ElementTree(root)

    print(root.tag)

    print(root[0].text)
    print(root[0].get('class'))

    html = """
        <html>
            <body>
                <div id='test' class='style1 style2'>
                    <span id='span1'>
                        span0
                        span1
                    </span>
                    <span id='span2'>span2</span>
                    <span class='span3'>span3</span>
                    <b><!-- 这里是注释 --></b>
            </body>
        </html>
    """

    """
    tag 对象 使用soup.tag_name(属性名)
    """
    soup = BeautifulSoup(html, 'lxml')
    # 多值属性，会返回一个list类型数据,同时可以设置多值属性
    soup.div['class'] = ['style3','style4']
    print(soup.div['class'])

    """
    navigableString:字符串常常包含在tag内，使用这个类来进行包装。
    """
    span_string = soup.span.string
    print(type(span_string))
    # tag中的字符串不可以被编辑，但是可以被替换
    # soup.span.string.replace_with('replace span1')
    # print(soup.span.string)

    """
    BeautifulSoup 它表示一个文档的全部内容
    """
    print(soup.name)

    """
    Comment 注释以及特殊字符串
    """
    print(type(soup.b.string))

    """
    遍历文档树
    """
    # contents children 只包含tag的直接子节点
    div_contents = soup.div.constents

    for item in soup.div.children:
        print(item)

    # .descendants 包含所有的子节点
    for child in soup.div.descendants:
        print(child)

    # .strings 返回是一个生成器 generator
    # stripped_strings 会自动去除空白的行，段首和段末的空白会被删除
    for string in soup.span.stripped_strings:
        print(string)

    """
    搜索文档树  find() find_all()
    """
    # 入参为字符串
    print(soup.find_all('span'))
    # 入参为 正则表达式
    import re
    print(soup.find_all(re.compile('^b')))
    # 入参为列表
    print(soup.find_all(['span','b']))
    # True 可以匹配任何值，但不会返回字符串节点
    print(soup.find_all(True))

    print('=' * 12)
    # print(soup.find(id='span2'))
    print(soup.find(class_='span3'))
    print(soup.find(attrs={'id':'span2'}))






















