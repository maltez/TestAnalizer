from SummaryDetail import SummaryDetail


class SummaryGetDetail(SummaryDetail):
    def __init__(self, url, request_parameters):
        SummaryDetail.__init__(self, url=url, type='GET')
        self.request_parameters = request_parameters