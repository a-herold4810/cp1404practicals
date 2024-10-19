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

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    countries = process_countries(data)
    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def load_data(filename):
    """ Loads CSV data from a file, skips the header row and returns as a list of rows """

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = list(reader)[1:]
    return data


def process_champions(data):
    """ Process the data to count how many times each champion has won """

    champions = {}
    for row in data:
        champion = row[2].strip()
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def process_countries(data):
    """ Process the data to extract the countries of the champions """

    countries = set()
    for row in data:
        country = row[1].strip()
        countries.add(country)
    return countries


main()
