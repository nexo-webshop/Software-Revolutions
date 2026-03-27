class DependencyResolver:
    def __init__(self):
        self.graph = {}

    def add_dependency(self, project, dep):
        self.graph.setdefault(project, []).append(dep)

    def resolve(self, project):
        # topological sort (belangrijk!)
        pass
