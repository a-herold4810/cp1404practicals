"""
Guitar
Estimate: 30 minutes
Start Time: 2035
Actual:
Finish Time:
"""


class Guitar:
    """ Represent a Guitar object """

    def __init__(self, name, year, cost=0):
        """ Initialise a Guitar instance with name, year, and cost attributes """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Return a string representation of the Guitar object """

        return f"{self.name} ({self.year}), worth ${self.cost:,.2f}"

    def get_age(self):
        """ Return the age of the guitar based on the current year """

        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """ Return True if the guitar is 50 or more years old """

        return self.get_age() >= 50

    def __lt__(self, other):
        """ Compare guitars by year for sorting """

        return self.year < other.year
