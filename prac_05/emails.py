"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

def main():
    """ Continuously prompts user for to enter an email address until a blank is entered """

    emails = []

    while True:
        email = input("Email: ")
        if email == "":
            break
        name = extract_name_from_email(email)
        print(f"Name: {name}")
        emails.append(email)

    print("Emails collected:")
    for email in emails:
        print(email)


def extract_name_from_email(email):
    """ Extracts name from provided email address, by splitting at @ and . or _ """

    name_part = email.split("@")[0]
    name = " ".join(part.title() for part in name_part.split("." or "_"))
    return name


main()
