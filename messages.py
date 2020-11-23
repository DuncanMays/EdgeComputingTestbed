
from local_config import SELF_IP_ADDRESS

class Message():
    """Base Message Class"""
    def __init__(self):
        self.type = ""

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Join(Message):
    """Initialization message sent by worker."""
    def __init__(self, data=None):
        super().__init__()
        self.type = "join"
        self.ip = SELF_IP_ADDRESS

        if data:
            self.__dict__ = data

class Leave(Message):
    """Initialization message sent by worker."""
    def __init__(self, data=None):
        super().__init__()
        self.type = "Leave"
        self.ip = SELF_IP_ADDRESS

        if data:
            self.__dict__ = data

def test(parameter):
    return parameter

class Task(Message):
    """Initialization message sent by worker."""
    def __init__(self, data=None):
        super().__init__()
        self.type = "task"
        self.ip = SELF_IP_ADDRESS

        self.workfn = test
        self.params = 'this is a test'

        if data:
            self.__dict__ = data
