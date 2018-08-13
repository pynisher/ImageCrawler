import urllib.parse
from Crawler.CssFinder import CssFinder


class Css:

    def __init__(self, page_url):

        self.page_url = page_url
        urlres = urllib.parse.urlparse(page_url)
        self.base_url = urlres.netloc
        self.styles = set()

    def fetch_links(self):

        img_finder = CssFinder(self.page_url)
        img_finder.feed(img_finder.html_string())
        self.styles = img_finder.get_values()
        return self.styles
