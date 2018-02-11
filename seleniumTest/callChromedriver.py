from selenium import webdriver
# ChromeDriver 需要设置环境变量，最简单的方法，是将ChromeDriver.exe文件放大到python安装目录下，与python 使用相同的环境变量
# 第二种方式是绝对地址调用chromedriver
# import os
# path = r'E:\Program Files\chromedriver\chromedriver.exe'
# abspath = os.path.abspath(path)
# dr = webdriver.Chrome(abspath)
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
dr.get("http://www.weibo.com")
print(dr.title)

