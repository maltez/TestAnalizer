__author__ = 'nickolay.lototskiy'
import json


class RequestResult:
    def __init__(self, url, type, body, params, elapsedTime, contentLength):
        self.url = url
        self.type = type
        if body is not None:
            self.body = json.loads(body)
        self.params = params
        self.elapsedTime = float(elapsedTime)
        self.contentLength = int(contentLength)

    def to_json(self):
        return {'url': self.url, 'type': self.type, 'body':self.body, 'elapsedTime':self.elapsedTime, 'contentLength': self.contentLength}