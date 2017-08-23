import requests
from bs4 import BeautifulSoup
class ItestVedioWebCrawler:
    def __init__(self):
        self.url = "http://www.itest.info/videos"
        self.html_doc = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_doc, "html.parser")

    def get_all_titles(self):
        title = []
        titles = self.soup.find_all("a", class_="video-link")
        #print(titles)
        for a in titles:
            title.append(a.string)
        return title

if __name__ == '__main__':
    title = ItestVedioWebCrawler().get_all_titles()
    print(title)