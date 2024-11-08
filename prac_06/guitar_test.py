"""
Guitar Test
Estimate: 55 minutes
Start Time: 1330
Actual: 40 minutes
Finish Time: 1410
"""

from guitar import Guitar

def run_tests():
    """ Test the functionality of the Guitar class """
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 1512.9)

    print(gibson)
    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")

    print(another_guitar)
    print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

run_tests()