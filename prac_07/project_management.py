"""
Project Management Program
Estimate: 90 minutes
Start Time: 0721
Actual:
Finish Time:
"""

FILENAME = "projects.txt"


def main():
    """ Main program function to manage projects """

    projects = load_projects()
    print("Projects loaded from file:")
    display_projects(projects)


def load_projects(filename=FILENAME):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, percent_complete = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    return projects


def display_projects(projects):
    """Display projects in a readable format."""
    for project in projects:
        print(project)


main()
