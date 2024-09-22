MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(score)
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        score = int(input("Enter score: "))
    return score


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def display_stars(score):
    """ Print asterisks for the length of the password passed in. """
    print("*" * score)

main()
