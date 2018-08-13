from UrlFinder import UrlFinder


class CssFinder(UrlFinder):

    def __init__(self, page_url):
        UrlFinder.__init__(self, page_url, 'link', 'href')
