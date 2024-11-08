"""
Guitar
Estimate: 30 minutes
Start Time: 2035
Actual: 35
Finish Time: 2110
"""

import csv
from guitar import Guitar


def main():
    """ Main function to load, sort, and display guitars """

    guitars = load_guitars()
    print("Guitars loaded from file:")
    for guitar in guitars:
        print(guitar)

    # Prompt user to add new guitars
    add_more = input("\nWould you like to add a new guitar? (y/n): ").lower()
    while add_more == 'y':
        new_guitar = add_guitar()
        guitars.append(new_guitar)
        add_more = input("Would you like to add another guitar? (y/n): ").lower()

    # Sort guitars by year and display
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    # Save updated list of guitars back to the CSV file
    save_guitars(guitars)



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


def add_guitar():
    """ Prompt the user to add a new guitar and return a Guitar object """

    name = input("Enter guitar name: ")
    year = int(input("Enter guitar year: "))
    cost = float(input("Enter guitar cost: "))
    return Guitar(name, year, cost)

def save_guitars(guitars, filename="guitars.csv"):
    """ Save the list of Guitar objects to a CSV file """

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Year", "Cost"])  # Write header
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
main()
