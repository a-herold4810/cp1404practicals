"""
Wimbledon
Estimate: 40 minutes
Actual:
"""
import csv

def main():
    filename = "wimbledon.csv"
    data = load_data(filename)
    champions = process_champions(data)
    print(champions)


def load_data(filename):
    """ Loads CSV data from a file, skips the header row and returns as a list of rows """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = list(reader)
    return data


def process_champions(data):
    champions = {}
    for row in data:
        champion = row[2].strip()
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions

main()
