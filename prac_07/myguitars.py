"""
Guitar
Estimate: 30 minutes
Start Time: 2035
Actual:
Finish Time:
"""

import csv
from guitar import Guitar


def main():
    """ Main function to load, sort, and display guitars """

    guitars = load_guitars()
    print("Guitars loaded from file:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename="guitars.csv"):
    """ Load guitars from a CSV file and return a list of Guitar objects """

    guitars = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


main()
