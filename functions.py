from classes import User, ConstructionManager, Project

def add_project(project, filename='projects.txt'):
    with open(filename, 'a') as file:
        file.write(f"{project.name},{project.address},{project.id},{project.manager},{project.po},{project.invoice}\n")

def list_projects(filename='projects.txt'):
    projects = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 6:
                    name, address, id, manager, po, invoice = data
                    project = Project(name, address, id, manager, po, invoice)
                    projects.append(project)
    except FileNotFoundError:
        pass
    return projects
