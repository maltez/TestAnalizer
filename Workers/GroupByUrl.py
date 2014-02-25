__author__ = 'nickolay.lototskiy'
import sys
sys.path.append('../BusinesObjects/')
from GroupedByUrlItem import GroupedByUrlItem


class GroupByUrl:

    def __init__(self):
        return


    @staticmethod
    def grouped_by_url(requests):
        output = []
        for item in requests:
            is_present = False
            for groupedItem in output:
                if groupedItem.url == item.url:
                    groupedItem.grouped_requests.append(item)
                    is_present = True
            if is_present:
                continue
            else:
                new_group = GroupedByUrlItem(item.url)
                new_group.grouped_requests.append(item)
                output.append(new_group)

        return output