import json

class Request:
    def __init__(self, status, data, message=''):
        self.status = status
        self.data = data
        self.message = message
