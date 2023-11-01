from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str

    def to_dict(self):
        return {'role': self.role, 'content': self.content}

    def __repr__(self):
        return str(self.to_dict())


class SystemMessage(Message):
    role: str = 'system'

    def __init__(self, content: str):
        self.content = content


class UserMessage(Message):
    role: str = 'user'

    def __init__(self, content: str):
        self.content = content
