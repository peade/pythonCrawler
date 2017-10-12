# coding=utf8
import os
import re
import time
import logging
import pdfkit
import requests
from bs4 import BeautifulSoup

htmlTpl = """
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


def url_to_html(url, name):
    """
    通过URL，获取HTML内容
    :param url :html的url
    :param name :html文件名
    """
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html5lib')
        body = soup.find_all(class_="article-intro")[0]
        html = str(body)

        def func(m):
            if not m.group(2).startswith("http"):
                rtn = m.group(1) + "http://www.runoob.com" + m.group(2) + m.group(3)
                return rtn
            else:
                return m.group(1) + m.group(2) + m.group(3)
                # body中的img标签的src相对路径的改成绝对路径

        pattern = "(<img .*?src=\")(.*?)(\")"

        html = re.compile(pattern).sub(func, html)
        html = htmlTpl.format(content=html)
        html = html.encode("utf-8")
        with open(name, 'wb') as f:
            f.write(html)
        return name
    except Exception as e:
        logging.error("解析错误", exc_info=True)


def getUrlList():
    """
    获取所有URL目录列表
    :return:
    """
    response = requests.get("http://www.runoob.com/htmldom/htmldom-methods.html")
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="design")[0]
    urls = []
    for a in menu_tag.find_all("a"):
        aUrl = a.get('href')
        url = "http://www.runoob.com" + aUrl
        urls.append(url)
        # if aUrl.startswith('/htmldom'):
        #     url = "http://www.runoob.com" + aUrl
        #     urls.append(url)

    return urls


def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
         'outline-depth': 10
    }
    # linux下单独配置 wkhtmltopdf  安装wkhtmlpdf为*not* using wkhtmltopdf patched qt.
    # 从官网下载 wkhtmltopdf 解压到本地文件夹，配置进去
    config=pdfkit.configuration(wkhtmltopdf='/home/lhf/programmes/wkhtmltox/bin/wkhtmltopdf')
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)

    # 安装wkhtmltopdf using patched qt 成功时用
   # pdfkit.from_file(htmls, file_name, options=options)

def main():
    start = time.time()
    urls = getUrlList()
    file_name = u"htmlDom.pdf"
    htmls = [url_to_html(url, str(index) + ".html") for index, url in enumerate(urls)]
    save_pdf(htmls, file_name)

    for html in htmls:
        os.remove(html)

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)


if __name__ == '__main__':
    main()
