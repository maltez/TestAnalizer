__author__ = 'nickolay.lototskiy'
from GroupedRequestBase import GroupedRequestBase
import json


class GroupedByUrlItem(GroupedRequestBase):
    def __init__(self, url):
        GroupedRequestBase.__init__(self)
        self.url = url

    def __str__(self):
        position = self.url.index('api')
        return self.url[position:]

    def to_json(self):
        return {'url':self.url,
                'min' : self.get_minimum,
                'max': self.get_maximum,
                'med':self.get_median,
                'requests': json.dumps([rep.to_json() for rep in self.grouped_requests])}