import urllib.request
import urllib.parse
from Crawler.LinkFinder import LinkFinder


class Page:

    def __init__(self, page_url):

        self.page_url = page_url
        urlres = urllib.parse.urlparse(page_url)
        self.base_url = urlres.netloc
        self.scheme = urlres.scheme
        self.links = set()

    def fetch_links(self):

        url_finder = LinkFinder(self.page_url)
        url_finder.feed(url_finder.html_string())
        self.links = url_finder.get_values()
        return self.links
