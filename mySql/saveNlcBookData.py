import requests
from bs4 import BeautifulSoup
import re

titleList = ['题名与责任', '著者', '出版项', '主题', '中图分类号', '版本项', '丛编项', '内容提要',
             '载体形态项', '一般附注']

# print('$'.join(titleList))

# CLC = "g25*" AND WFM = ( BK )
# ( CLC = "g25*" AND WFM = ( BK ) ) and ( WYR = ( 2011 -> 2018 ) )
# ( CLC = "g25*" AND WFM = ( BK ) ) and ( WYR = 2015 )
def get_lisk_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tds = soup.find_all(class_=re.compile("itemtitle"))
    for i in tds:
        # print(i.find('a').get('href'))
        bookLink = i.find('a').get('href')
        getBookDetails(bookLink)
        # print('-------------------------------------------------------------------------')


def getBookDetails(link):
    # print(link)
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    table = soup.find('table', id='td')
    trs = table.find_all('tr')
    str = ''
    curName = ''
    bookInfo = ['', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '']
    for tr in trs:
        td1 = tr.find_all('td')[0].get_text().strip()
        td2 = tr.find_all('td')[1].get_text().strip()
        if not td2:
            continue
        if td1 and not td1 in titleList:
            print(td1)
            titleList.append(td1)
            bookInfo.append('')
        if curName:
            if curName == td1 or not td1:
                index = titleList.index(curName)
                bookInfo[index] = bookInfo[index] + '|' + td2
            else:
                index = titleList.index(td1)
                bookInfo[index] = td2
                curName = td1
        else:
            curName = td1
            bookInfo[0] = td2
            # if curName:
            #     if curName == td1 or not td1:
            #         #str = str + ';' + td2
            #     else:
            #         lastIndex = titleList.index(curName)
            #         curIndex = titleList.index(td1)
            #         #str = str + '$' * (abs(curIndex - lastIndex)) + td2
            # else:
            #     curName = td1
            # str += td2
            # if (tds.index(i) % 2 == 1):
            #     str = str + i.get_text().strip() + "$$"
    print('$'.join(bookInfo))


def main():
    jump = 221
    for i in range(100):
        link = 'http://opac.nlc.cn:80/F/AC61FI94VN1NE6IG8YPN9R9UXACVQDKRRD5LFAD898NAVCSSU6-12767?func=short-jump&jump=' \
               + str(jump)
        print(jump)
        get_lisk_link(link)
        jump += 10


if __name__ == '__main__':
    main()
