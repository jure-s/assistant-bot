class Note:
    def __init__(self, content, tags=None):
        self.content = content
        self.tags = tags or []

    def __str__(self):
        tags = ", ".join(self.tags) if self.tags else "No tags"
        return f"Note: {self.content}, Tags: {tags}"