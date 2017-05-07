import json


class BaseRouter:
    def __init__(self):
        self.message = ''
        self.result = ''

    def set_message(self, message):
        if type(message) == str:
            self.message = json.loads(message)
        elif type(message) == dict:
            self.message = message
        else:
            raise TypeError()
        return self

    def _do_rpc(self):
        raise NotImplemented

    def rpc(self):
        self._do_rpc()
        if type(self.result) != str:
            print(self.result)
            self.result = json.dumps(self.result)
        return self.result
