class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

class ConstructionManager(User):
    def __init__(self, username, email, projects=None):
        super().__init__(username, email)
        self.projects = projects if projects else []

    def add_project(self, project):
        self.projects.append(project)

    def list_projects(self):
        print(f"Projects managed by {self.username}:")
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. Project Name: {project.name}, Budget: {project.budget}")

class Project:
    def __init__(self, name, address, id, manager, po, invoice):
        self.name = name
        self.address = address
        self.id = id
        self.manager = manager
        self.po = po
        self.invoice = invoice
