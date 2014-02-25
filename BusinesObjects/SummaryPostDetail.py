from SummaryDetail import SummaryDetail
import json


class SummaryPostDetail(SummaryDetail):
    def __init__(self, url, body):
        SummaryDetail.__init__(self, url=url, type='POST')
        parsed_body = json.loads(body)
        self.body = parsed_body