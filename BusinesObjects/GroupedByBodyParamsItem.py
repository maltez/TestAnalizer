__author__ = 'nickolay.lototskiy'
from GroupedRequestBase import GroupedRequestBase


class GroupedByBodyParamsItem(GroupedRequestBase):
    def __init__(self, params):
        GroupedRequestBase.__init__(self)
        self.params = params
        self.values = dict()
        for param in params:
            self.values[param] = ''