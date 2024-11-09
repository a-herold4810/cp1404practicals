"""
Project Management Program
Estimate: 90 minutes
Start Time: 0721
Actual:
Finish Time:
"""

import csv
import datetime

from project import Project

FILENAME = "projects.txt"


def main():
    """ Main program function to manage projects """

    projects = load_projects()

    while True:
        print("\nMenu:")
        print("(D)isplay projects by completion")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(Q)uit")
        choice = input(">>> ").lower()

        if choice == 'd':
            incomplete_projects = filter_projects_by_completion(projects, complete=False)
            complete_projects = filter_projects_by_completion(projects, complete=True)
            print("\nIncomplete projects:")
            display_projects(incomplete_projects)
            print("\nComplete projects:")
            display_projects(complete_projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
            filtered_projects = filter_projects_by_start_date(projects, date)
            print("\nFiltered projects by start date:")
            display_projects(filtered_projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
            print("New project added.")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def load_projects(filename=FILENAME):
    """ Load projects from a file and return a list of Project objects"""

    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, percent_complete = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    return projects


def display_projects(projects):
    """ Display projects in a readable format """

    for project in projects:
        print(project)


def filter_projects_by_completion(projects, complete=True):
    """ Filter projects by completion status """

    return [project for project in projects if project.is_complete() == complete]


def filter_projects_by_start_date(projects, date):
    """ Filter projects that start after the specified date """

    return [project for project in projects if project.starts_after(date)]


def add_new_project():
    """ Prompt the user to add a new project and return a Project object """

    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


main()
