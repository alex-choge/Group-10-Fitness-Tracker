class Goal:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "not done"

    def complete(self):
        self.status = "done"
        print("Goal completed!")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    def __str__(self):
        return f"{self.title}: {self.description} [{self.status}]"
