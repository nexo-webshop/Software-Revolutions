class ProjectManager:
    def __init__(self):
        self.projects = {}
        self.active_project = None

    def create_project(self, name, path):
        project = Project(name, path)
        self.projects[name] = project
        return project

    def load_project(self, path):
        project = Project.load(path)
        self.projects[project.name] = project
        return project

    def set_active(self, name):
        self.active_project = self.projects.get(name)
