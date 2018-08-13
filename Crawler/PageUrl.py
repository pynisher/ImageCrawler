import urllib.parse


class PageUrl:

    def __init__(self, init_val=None, name='page_url'):

        self.val = init_val
        self.name = name

    def __get__(self, obj, objtype):

        return self.val

    def __set__(self, obj, val):
        result = urllib.parse.urlparse(val)

        if len(result.scheme) > 0 and len(result.netloc) > 0:
            self.val = 'OOOO'
        else:
            print('Invalid')
            raise Exception('Url is not valid')
