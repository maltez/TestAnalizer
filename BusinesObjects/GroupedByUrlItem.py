__author__ = 'nickolay.lototskiy'
from GroupedRequestBase import GroupedRequestBase


class GroupedByUrlItem(GroupedRequestBase):
    def __init__(self, url):
        GroupedRequestBase.__init__(self)
        self.url = url