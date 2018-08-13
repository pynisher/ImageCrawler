import urllib.parse
from Crawler.ImgFinder import ImgFinder


class Image:

    def __init__(self, page_url):

        self.page_url = page_url
        urlres = urllib.parse.urlparse(page_url)
        self.base_url = urlres.netloc
        self.images = set()

    def fetch_links(self):

        img_finder = ImgFinder(self.page_url)
        img_finder.feed(img_finder.html_string())
        self.images = img_finder.get_values()
        return self.images

