import requests
from bs4 import BeautifulSoup

class DoubanWebCrawler:

    def __init__(self):
        self.url = 'https://book.douban.com/'
        self.html_doc = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_doc,  "html.parser")

    def get_popular_books(self):
        res = []

        for li in self.soup.find('ul', class_='list-summary').find_all('li'):
            book = {}
            book['title'] = li.find('h4', class_='title').get_text()
            book['rating'] = li.find('span', class_='average-rating').get_text().strip()
            #print(book)
            res.append(book)
        return res

if __name__ == '__main__':
    titles = DoubanWebCrawler().get_popular_books()
    print(titles)