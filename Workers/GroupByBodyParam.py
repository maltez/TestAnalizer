__author__ = 'nickolay.lototskiy'
import sys

sys.path.append('../BusinesObjects/')
from GroupedByUrlSimpleItem import GroupedByUrlSimpleItem
from GroupedByUrlItem import GroupedByUrlItem
from GroupedByBodyParamsItem import GroupedByBodyParamsItem


class GroupByBodyParam:
    def __init__(self):
        pass

    @staticmethod
    def GroupByBodyParam(grouped_by_url, params):
        output = []
        for item in grouped_by_url:
            new_group_item = GroupedByUrlSimpleItem(item.url)
            new_group_item.requests = []
            for request in item.grouped_requests:
                has_param = True
                for param in params:
                    has_param &= hasattr(request.body, param)

                if has_param:
                    is_present_in_collection = True
                    for groupedRequest in new_group_item.requests:
                        for param in params:
                            is_present_in_collection &= groupedRequest.values[param] == request.body[param]
                        if is_present_in_collection:
                            groupedRequest.grouped_requests.append(request)
                        else:
                            new_group = GroupedByBodyParamsItem(params)
                            for param in params:
                                new_group.values[param] = request.body[param]
                            new_group_item.requests.append(new_group)
            output.append(new_group_item)

        return output