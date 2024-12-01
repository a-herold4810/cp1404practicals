"""
Emails
Estimate: 30 minutes
Actual: 27 minutes
"""

def main():
    """ Continuously prompts user for to enter an email address until a blank is entered """

    email_dict = {}

    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name_from_email(email)

        correct_name = input(f"Is your name {name}? (Y/n) ").lower()

        if correct_name == "n" or correct_name == "no":
            name = input("Name: ")

        email_dict[email] = name

    print()
    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """ Extracts name from provided email address, by splitting at @ and . or _ """

    name_part = email.split("@")[0]
    name = " ".join(part.title() for part in name_part.split("." or "_"))
    return name


main()
