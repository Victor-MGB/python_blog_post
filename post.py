from datetime import datetime

class Post():
    """docstring for ClassName."""
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now()
        
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nTimestamp: {self.timestamp}\n"

    