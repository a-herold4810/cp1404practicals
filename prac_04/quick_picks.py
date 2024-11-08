import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

quick_picks_count = int(input("How many quick picks? "))

for _ in range(quick_picks_count):
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()

    for number in quick_pick:
        print(f"{number:2}", end=" ")
    print()