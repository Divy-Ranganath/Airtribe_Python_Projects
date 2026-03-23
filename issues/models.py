from abc import ABC, abstractmethod

class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }

class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):
        if not self.name:
            raise ValueError('Name cannot be empty')
        if '@' not in self.email:
            raise ValueError('Invalid email')
        
class Issue(BaseEntity):
    def __init__(self, id, title, description, status, priority, reporter_id):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id

    def validate(self):
        if not self.title:
            raise ValueError('Title cannot be empty')
        
        given_priority = ["low", "medium", "high", "critical"]
        if self.priority not in given_priority:
            raise ValueError('Priority must be one of - low, medium, high, critical')
        
        given_status = ["open", "in_progress", "resolved", "closed"]
        if self.status not in given_status:
            raise ValueError('Status must be one of - open, in_progress, resolved, closed')


    def describe(self):
        return f"{self.title} [{self.priority}]"

class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT] {self.title} — needs immediate attention"

class LowPriorityIssue(Issue):
    def describe(self):
        return f"{self.title} — low priority, handle when free"
