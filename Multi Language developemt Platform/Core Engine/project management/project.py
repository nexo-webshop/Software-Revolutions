class Project:
    def __init__(self, name, root_path):
        self.name = name
        self.root_path = root_path
        self.config = None
        self.workspace = None
        self.dependencies = []

    @staticmethod
    def load(path):
        # laad config + structuur
        pass

    def save(self):
        # schrijf config naar disk
        pass
