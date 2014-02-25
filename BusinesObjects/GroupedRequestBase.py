__author__ = 'nickolay.lototskiy'


class GroupedRequestBase:
    def __init__(self):
        self.grouped_requests = []

    @property
    def get_minimum(self):
        minimum = 0
        if len(self.grouped_requests) != 0:
            minimum = self.grouped_requests[0].elapsedTime
        else:
            return minimum

        for item in self.grouped_requests:
            if item.elapsedTime < minimum:
                minimum = item.elapsedTime

        return minimum

    @property
    def get_maximum(self):
        maximum = 0
        if len(self.grouped_requests) != 0:
            maximum = self.grouped_requests[0].elapsedTime
        else:
            return maximum

        for item in self.grouped_requests:
            if item.elapsedTime > maximum:
                maximum = item.elapsedTime

        return maximum

    @property
    def get_median(self):
        median = 0
        total = 0
        count = len(self.grouped_requests)
        for item in self.grouped_requests:
            total = total + item.elapsedTime

        if count > 0:
            median = total / count

        return median