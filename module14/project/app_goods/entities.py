

class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def to_dict(self):
        return dict(
            name=self.name,
            description=self.description,
            weigh=self.weight
            )