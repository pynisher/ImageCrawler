import os.path
from Image import Save


class Download:
    folder = 'storage/'

    def __init__(self, take=None, links={}, path="images"):

        self.limit = take
        self.path = self.folder + path
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.links = links

    def start(self) -> object:

        if isinstance(self.limit, int) and len(self.links) >= self.limit:
            links = sorted(self.links)[0:self.limit]
        else:
            links = self.links

        for file in links:
            try:
                img = Save.Save(file, self.path)
                img.save()
            except Exception as e:
                print(str(e))
        return self
