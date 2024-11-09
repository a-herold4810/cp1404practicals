"""
Project Management Program
Estimate: 90 minutes
Start Time: 0721
Actual: 1h 54 minutes
Finish Time: 0915
"""

from datetime import datetime


class Project:
    """ Represent a Project with details such as name, start date, priority, cost estimate, and completion percentage """

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """ Initialise a Project instance """

        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        """ Return a string representation of the Project """

        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, "
                f"estimated: ${self.cost_estimate:,.2f}, completion: {self.percent_complete}%")

    def __lt__(self, other):
        """ Compare projects by priority for sorting"""

        return self.priority < other.priority

    def is_complete(self):
        """ Return True if the project is 100% complete """

        return self.percent_complete == 100

    def starts_after(self, date):
        """ Return True if the project starts after the specified date """

        return self.start_date > date
