# main.py

from classes import User, ConstructionManager, Project
from functions import add_project, list_projects
import gui  

def main():
    user = User("JohnDoe", "johndoe@example.com")
    construction_manager = ConstructionManager("ConstructionMgr", "mgr@example.com")

    while True:
        print("\nConstruction Management POC")
        print("1. Add Project")
        print("2. List Projects")
        print("3. Display User Info")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Use the GUI module to get project information
            name, address, id, manager, po, invoice = gui.get_project_info()

            # Create a Project object and add it to the data storage
            project = Project(name, address, id, manager, po, invoice)
            add_project(project)
            print("Project added successfully!")

        elif choice == '2':
            projects = list_projects()
            if projects:
                print("\nList of Projects:")
                for idx, project in enumerate(projects, start=1):
                    print(f"{idx}. Project Name: {project.name}, Address: {project.address}, ID: {project.id}, Manager: {project.manager}, PO: {project.po}, Invoice: {project.invoice}")
            else:
                print("No projects found.")

        elif choice == '3':
            user.display_info()

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
