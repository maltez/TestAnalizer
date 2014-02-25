__author__ = 'nickolay.lototskiy'


class GroupedByUrlSimpleItem:
    def __init__(self, url):
        self.url = url
        self.requests = []