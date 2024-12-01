MINIMUM_LENGTH = 8


def main():
    """ Get and print password using functions. """
    password = get_password()
    print_asterisks(password)


def get_password():
    """ Get password, making sure it is a minimum length. """
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password too short")
        password = input("Password: ")
    return password


def print_asterisks(password):
    """ Print asterisks for the length of the password passed in. """
    for letter in password:
        print("*", end="")
    print()


main()