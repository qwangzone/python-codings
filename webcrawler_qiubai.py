import requests
import sys
from bs4 import BeautifulSoup
class QiuBaiCrawler:
    def __init__(self, pages):
        self.pages = pages
        self.base_url = "https://www.qiushibaike.com/8hr/page/"



    def get_content(self):
        con = []
        for i in range(1, self.pages):
            self.url = self.base_url + str(i)
            self.html_doc = requests.get(self.url).text
            self.soup = BeautifulSoup(self.html_doc, "html.parser")

            contents = self.soup.find_all("div", class_="content")
            for a in contents:
               con.append(a.get_text())
            print (self.url)
        return con

if __name__=='__main__':
    #如果不传值或者传值正确的默认爬一页的数据
    pages = sys.argv
    if len(pages)!=2:
        page_num = 2
    elif pages[1].isdigit():
        page_num = int(pages[1])
    else:
        page_num = 2
    a = QiuBaiCrawler(page_num).get_content()
    for text in a:
        print(text)
    print(len(a))